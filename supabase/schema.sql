-- =====================================================================
-- Quiz Live - Schéma Supabase
-- Tables: quizzes, questions, answers, participants, responses
-- Realtime: quizzes, participants, responses
-- RLS: lecture publique + insert public sur participants/responses
-- =====================================================================

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------------
-- Tables
-- ---------------------------------------------------------------------

create table if not exists public.quizzes (
  id                      uuid primary key default gen_random_uuid(),
  title                   text not null,
  category                text check (category in ('HTML','CSS','JS','Java','Python','SQL')) default 'HTML',
  description             text,
  join_code               text unique not null,
  status                  text not null default 'draft' check (status in ('draft','waiting','live','finished')),
  current_question_index  int  not null default 0,
  created_at              timestamptz not null default now()
);

create table if not exists public.questions (
  id           uuid primary key default gen_random_uuid(),
  quiz_id      uuid not null references public.quizzes(id) on delete cascade,
  statement    text not null,
  type         text not null check (type in ('single','multiple','truefalse')),
  time_limit   int,
  order_index  int  not null default 0
);

create index if not exists questions_quiz_idx
  on public.questions(quiz_id, order_index);

create table if not exists public.answers (
  id           uuid primary key default gen_random_uuid(),
  question_id  uuid not null references public.questions(id) on delete cascade,
  text         text not null,
  is_correct   boolean not null default false
);

create index if not exists answers_question_idx
  on public.answers(question_id);

create table if not exists public.participants (
  id         uuid primary key default gen_random_uuid(),
  quiz_id    uuid not null references public.quizzes(id) on delete cascade,
  username   text not null,
  score      int  not null default 0,
  joined_at  timestamptz not null default now(),
  unique (quiz_id, username)
);

create index if not exists participants_quiz_idx
  on public.participants(quiz_id);

create table if not exists public.responses (
  id              uuid primary key default gen_random_uuid(),
  participant_id  uuid not null references public.participants(id) on delete cascade,
  question_id     uuid not null references public.questions(id) on delete cascade,
  answer_ids      uuid[] not null default '{}',
  is_correct      boolean not null default false,
  answered_at     timestamptz not null default now(),
  unique (participant_id, question_id)
);

create index if not exists responses_question_idx
  on public.responses(question_id);

-- ---------------------------------------------------------------------
-- Migration : catégories autorisées = HTML, CSS, JS, Java, Python, SQL
-- Idempotent : à rejouer même si la table existe déjà avec l'ancienne
-- contrainte (HTML/CSS/JS/C/SQL/IA/Autre). C'est ce qui bloquait la
-- création de quiz : un insert avec une catégorie hors de l'ancienne
-- liste violait la contrainte CHECK et faisait échouer toute la requête.
-- ---------------------------------------------------------------------

update public.quizzes
  set category = 'HTML'
  where category is null or category not in ('HTML','CSS','JS','Java','Python','SQL');

do $$
declare
  conname text;
begin
  for conname in
    select c.conname
    from pg_constraint c
    join pg_class t on t.oid = c.conrelid
    where t.relname = 'quizzes'
      and c.contype = 'c'
      and pg_get_constraintdef(c.oid) ilike '%category%'
  loop
    execute format('alter table public.quizzes drop constraint %I', conname);
  end loop;
end $$;

alter table public.quizzes
  add constraint quizzes_category_check
  check (category in ('HTML','CSS','JS','Java','Python','SQL'));

alter table public.quizzes
  alter column category set default 'HTML';

-- ---------------------------------------------------------------------
-- Realtime publication (idempotent)
-- ---------------------------------------------------------------------

do $$
declare
  t text;
begin
  foreach t in array array['quizzes','participants','responses']
  loop
    if not exists (
      select 1
      from pg_publication_tables
      where pubname = 'supabase_realtime'
        and schemaname = 'public'
        and tablename = t
    ) then
      execute format('alter publication supabase_realtime add table public.%I', t);
    end if;
  end loop;
end $$;

-- ---------------------------------------------------------------------
-- Row Level Security
-- ---------------------------------------------------------------------

alter table public.quizzes      enable row level security;
alter table public.questions    enable row level security;
alter table public.answers      enable row level security;
alter table public.participants enable row level security;
alter table public.responses    enable row level security;

-- Lecture publique
drop policy if exists "public read quizzes"      on public.quizzes;
drop policy if exists "public read questions"    on public.questions;
drop policy if exists "public read answers"      on public.answers;
drop policy if exists "public read participants" on public.participants;
drop policy if exists "public read responses"    on public.responses;

create policy "public read quizzes"      on public.quizzes      for select using (true);
create policy "public read questions"    on public.questions    for select using (true);
create policy "public read answers"      on public.answers      for select using (true);
create policy "public read participants" on public.participants for select using (true);
create policy "public read responses"    on public.responses    for select using (true);

-- Insertion publique (participants & responses)
drop policy if exists "public insert participants" on public.participants;
drop policy if exists "public insert responses"    on public.responses;

create policy "public insert participants" on public.participants for insert with check (true);
create policy "public insert responses"    on public.responses    for insert with check (true);

-- Note: aucune politique UPDATE/DELETE pour anon → seules les routes API
-- utilisant SUPABASE_SERVICE_ROLE_KEY peuvent écrire (admin).
-- Le service_role bypasse RLS par défaut.

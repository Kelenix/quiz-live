/**
 * Quiz Live — Harnais de test de charge VISUEL (navigateur).
 *
 * À exécuter dans l'onglet du site déployé (même origine que /api), via la
 * console ou l'extension Chrome. Aucune clé secrète n'est stockée ici :
 * la configuration (dont la clé service_role) est fournie au lancement via
 * window.__LT_CFG, qui ne vit qu'en mémoire le temps du test.
 *
 *   window.__LT_CFG = {
 *     SUPA: "https://xxx.supabase.co",
 *     ANON: "<anon key>",
 *     SERVICE: "<service_role key>",  // créer / piloter / supprimer le quiz de test
 *     BASE: location.origin,           // origine des routes /api
 *     N: 1000,                         // nombre d'utilisateurs virtuels
 *     CONC: 60,                        // concurrence (requêtes simultanées)
 *     CLEANUP: true                    // supprimer le quiz de test à la fin
 *   };
 *   startLoadTest(window.__LT_CFG);
 *
 * Le harnais crée un quiz de 6 questions, fait rejoindre N joueurs via
 * /api/join, passe le quiz en direct, fait répondre tout le monde aux 6
 * questions via /api/responses, et — NOUVEAU — capture le CLASSEMENT APRÈS
 * CHAQUE QUESTION (pas seulement à la fin) en suivant aussi la position d'un
 * joueur témoin au fil du quiz. Tout est affiché en temps réel.
 * window.__loadtest expose l'état en direct (dont .snapshots et .report).
 */
(function () {
  "use strict";

  const QDEF = [
    { statement: "JavaScript est un langage à typage statique.", type: "truefalse", answers: [ { t: "Vrai", c: false }, { t: "Faux", c: true } ] },
    { statement: "Quel mot-clé déclare une constante en JavaScript ?", type: "single", answers: [ { t: "var", c: false }, { t: "let", c: false }, { t: "const", c: true }, { t: "define", c: false } ] },
    { statement: "Quelle méthode ajoute un élément à la fin d'un tableau ?", type: "single", answers: [ { t: "push()", c: true }, { t: "pop()", c: false }, { t: "shift()", c: false }, { t: "unshift()", c: false } ] },
    { statement: "Lesquels sont des types primitifs en JavaScript ?", type: "multiple", answers: [ { t: "string", c: true }, { t: "number", c: true }, { t: "boolean", c: true }, { t: "object", c: false } ] },
    { statement: "L'opérateur === compare la valeur ET le type.", type: "truefalse", answers: [ { t: "Vrai", c: true }, { t: "Faux", c: false } ] },
    { statement: "Que retourne typeof null ?", type: "single", answers: [ { t: '"null"', c: false }, { t: '"object"', c: true }, { t: '"undefined"', c: false }, { t: '"number"', c: false } ] },
  ];
  const TIME_LIMIT = 20;
  const AB = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const genCode = (n) => { let s = ""; for (let i = 0; i < n; i++) s += AB[Math.floor(Math.random() * AB.length)]; return s; };
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const rint = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const pct = (arr, p) => { if (!arr.length) return 0; const s = [...arr].sort((x, y) => x - y); return s[Math.min(s.length - 1, Math.floor((p / 100) * s.length))]; };
  const avg = (a) => (a.length ? Math.round(a.reduce((x, y) => x + y, 0) / a.length) : 0);
  async function pool(items, conc, fn) { let i = 0; const w = new Array(Math.min(conc, items.length)).fill(0).map(async () => { while (i < items.length) { const idx = i++; await fn(items[idx], idx); } }); await Promise.all(w); }

  const ST = (window.__loadtest = { phase: "init", done: false, error: null, quizId: null, code: null, joined: 0, joinErrors: 0, responsesOk: 0, responsesErr: 0, correct: 0, partial: 0, lat: { join: [], resp: [] }, perQuestion: [], snapshots: [], trackName: null, leaderboard: [], report: null, startedAt: Date.now() });

  let UI = {};
  function buildUI(N) {
    const root = document.createElement("div"); root.id = "lt-root";
    const side = Math.ceil(Math.sqrt(N * 1.6));
    root.innerHTML = `
      <style>
        #lt-root{position:fixed;inset:0;z-index:999999;background:#0b0f0d;color:#e6efe9;font-family:Inter,system-ui,Arial,sans-serif;overflow:auto;padding:18px 22px}
        #lt-root *{box-sizing:border-box}
        .lt-h{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:6px}
        .lt-h h1{font-size:19px;margin:0;font-weight:700}
        .lt-badge{font-size:12px;padding:3px 10px;border-radius:999px;border:1px solid #1f9d63;background:rgba(62,207,142,.12);color:#3ecf8e;font-weight:600}
        .lt-sub{color:#7d8c84;font-size:12.5px;margin:0 0 14px}
        .lt-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
        .lt-card{background:#121815;border:1px solid #1d2722;border-radius:12px;padding:10px 12px}
        .lt-card .k{font-size:11px;color:#7d8c84;text-transform:uppercase;letter-spacing:.04em}
        .lt-card .v{font-size:22px;font-weight:700;margin-top:2px}
        .lt-card .v small{font-size:12px;color:#7d8c84;font-weight:500}
        .lt-bar{height:8px;border-radius:6px;background:#1d2722;overflow:hidden;margin:10px 0 14px}
        .lt-bar>i{display:block;height:100%;width:0;background:linear-gradient(90deg,#3ecf8e,#1f9d63);transition:width .25s}
        .lt-grid{display:grid;grid-template-columns:repeat(${side},1fr);gap:2px;margin-bottom:16px}
        .lt-cell{aspect-ratio:1;border-radius:2px;background:#171f1b;border:1px solid #222e28;transition:all .1s}
        .lt-cell.join{border-color:#3ecf8e;background:#16261e}
        .lt-cell.send{background:#13314a;border-color:#3b82f6}
        .lt-cell.ok{background:rgba(62,207,142,.32);border-color:#3ecf8e}
        .lt-cell.part{background:rgba(245,180,60,.30);border-color:#f5b43c}
        .lt-cell.bad{background:rgba(239,90,90,.30);border-color:#ef5a5a}
        .lt-cols{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;align-items:start}
        @media(max-width:980px){.lt-cols{grid-template-columns:1fr}}
        .lt-panel{background:#121815;border:1px solid #1d2722;border-radius:12px;padding:12px 14px}
        .lt-panel h3{margin:0 0 8px;font-size:13px;color:#9fb0a8;font-weight:600;text-transform:uppercase;letter-spacing:.04em}
        #lt-log{font-family:ui-monospace,Menlo,monospace;font-size:12px;line-height:1.55;max-height:300px;overflow:auto;color:#9fb0a8}
        #lt-log b{color:#3ecf8e}
        .lt-lb{width:100%;border-collapse:collapse;font-size:13px}
        .lt-lb td{padding:6px 8px;border-bottom:1px solid #1d2722}
        .lt-lb tr:first-child td{color:#3ecf8e;font-weight:700}
        .lt-rk{color:#7d8c84;width:34px}
        .lt-sc{text-align:right;font-weight:700}
        .lt-evo{font-size:12.5px;line-height:1.7}
        .lt-evo .row{display:flex;justify-content:space-between;gap:8px;border-bottom:1px solid #161e1a;padding:4px 0}
        .lt-evo .q{color:#9fb0a8}
        .lt-evo .lead{color:#3ecf8e;font-weight:600}
        .lt-evo .me{color:#7db3ff;font-weight:700}
        .lt-track{margin-top:8px;padding:8px 10px;border:1px dashed #2a4a63;border-radius:8px;background:rgba(59,130,246,.07);font-size:12.5px;color:#9cc3ec}
      </style>
      <div class="lt-h"><h1>⚡ Quiz Live — Test de charge</h1><span class="lt-badge" id="lt-phase">init</span><span class="lt-badge" id="lt-codebadge" style="border-color:#3b82f6;background:rgba(59,130,246,.12);color:#7db3ff">code —</span></div>
      <p class="lt-sub" id="lt-sub">${N} utilisateurs virtuels · quiz de 6 questions · classement mis à jour après CHAQUE question</p>
      <div class="lt-cards">
        <div class="lt-card"><div class="k">Connectés</div><div class="v"><span id="m-join">0</span><small>/${N}</small></div></div>
        <div class="lt-card"><div class="k">Réponses OK</div><div class="v" id="m-resp">0</div></div>
        <div class="lt-card"><div class="k">Erreurs</div><div class="v" id="m-err" style="color:#ef8a8a">0</div></div>
        <div class="lt-card"><div class="k">Latence moy.</div><div class="v"><span id="m-lat">0</span><small>ms</small></div></div>
        <div class="lt-card"><div class="k">Latence p95</div><div class="v"><span id="m-p95">0</span><small>ms</small></div></div>
        <div class="lt-card"><div class="k">Débit</div><div class="v"><span id="m-rps">0</span><small>req/s</small></div></div>
      </div>
      <div class="lt-bar"><i id="lt-prog"></i></div>
      <div class="lt-grid" id="lt-grid"></div>
      <div class="lt-cols">
        <div class="lt-panel"><h3>Journal en direct</h3><div id="lt-log"></div></div>
        <div class="lt-panel"><h3>Classement après chaque question</h3><div class="lt-evo" id="lt-evo" style="color:#7d8c84">Le classement s'affichera dès la 1ère question…</div><div class="lt-track" id="lt-track" style="display:none"></div></div>
        <div class="lt-panel"><h3>Classement final</h3><div id="lt-lbwrap" style="color:#7d8c84;font-size:13px">En attente de la fin du quiz…</div></div>
      </div>`;
    document.body.innerHTML = ""; document.body.appendChild(root);
    const cells = []; const grid = root.querySelector("#lt-grid");
    for (let i = 0; i < N; i++) { const c = document.createElement("div"); c.className = "lt-cell"; grid.appendChild(c); cells.push(c); }
    UI = { phase: root.querySelector("#lt-phase"), codebadge: root.querySelector("#lt-codebadge"), mJoin: root.querySelector("#m-join"), mResp: root.querySelector("#m-resp"), mErr: root.querySelector("#m-err"), mLat: root.querySelector("#m-lat"), mP95: root.querySelector("#m-p95"), mRps: root.querySelector("#m-rps"), prog: root.querySelector("#lt-prog"), log: root.querySelector("#lt-log"), evo: root.querySelector("#lt-evo"), track: root.querySelector("#lt-track"), lbwrap: root.querySelector("#lt-lbwrap"), cells };
  }
  function log(msg, hl) { const t = new Date().toLocaleTimeString(); const l = document.createElement("div"); l.innerHTML = `<span style="color:#566">[${t}]</span> ${hl ? "<b>" + msg + "</b>" : msg}`; UI.log.prepend(l); }
  const setPhase = (p) => { ST.phase = p; UI.phase.textContent = p; };
  const setProg = (f) => { UI.prog.style.width = Math.round(f * 100) + "%"; };
  function refreshMetrics() { const all = ST.lat.join.concat(ST.lat.resp); UI.mJoin.textContent = ST.joined; UI.mResp.textContent = ST.responsesOk; UI.mErr.textContent = ST.joinErrors + ST.responsesErr; UI.mLat.textContent = avg(all); UI.mP95.textContent = pct(all, 95); const secs = Math.max(0.001, (Date.now() - ST.startedAt) / 1000); UI.mRps.textContent = Math.round((ST.joined + ST.responsesOk + ST.joinErrors + ST.responsesErr) / secs); }

  const cfg = window.__LT_CFG;
  const svcH = () => ({ apikey: cfg.SERVICE, Authorization: `Bearer ${cfg.SERVICE}`, "Content-Type": "application/json", Prefer: "return=representation" });
  async function sb(method, path, body) { const r = await fetch(`${cfg.SUPA}/rest/v1/${path}`, { method, headers: svcH(), body: body ? JSON.stringify(body) : undefined }); if (!r.ok) throw new Error(`${method} ${path} -> ${r.status} ${await r.text()}`); const t = await r.text(); return t ? JSON.parse(t) : null; }
  async function createQuiz() { const code = genCode(6); ST.code = code; UI.codebadge.textContent = "code " + code; const quiz = (await sb("POST", "quizzes", { title: "LOADTEST — Quiz JS (test de charge)", category: "JS", description: "Quiz temporaire de test de charge.", join_code: code, status: "waiting", current_question_index: 0 }))[0]; ST.quizId = quiz.id; const qrows = await sb("POST", "questions", QDEF.map((q, idx) => ({ quiz_id: quiz.id, statement: q.statement, type: q.type, time_limit: TIME_LIMIT, order_index: idx }))); qrows.sort((a, b) => a.order_index - b.order_index); const questions = []; for (let i = 0; i < qrows.length; i++) { const def = QDEF[i]; const ar = await sb("POST", "answers", def.answers.map((a) => ({ question_id: qrows[i].id, text: a.t, is_correct: a.c }))); questions.push({ id: qrows[i].id, type: def.type, correct: ar.filter((a) => a.is_correct).map((a) => a.id), wrong: ar.filter((a) => !a.is_correct).map((a) => a.id) }); } return { questions }; }
  const patchQuiz = (f) => sb("PATCH", `quizzes?id=eq.${ST.quizId}`, f);

  async function joinAll(N) { const ids = new Array(N).fill(null); await pool([...Array(N).keys()], cfg.CONC, async (i) => { const cell = UI.cells[i]; cell.classList.add("send"); const t0 = performance.now(); try { const r = await fetch(`${cfg.BASE}/api/join/${ST.code}`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ username: `Joueur_${String(i + 1).padStart(4, "0")}` }) }); ST.lat.join.push(performance.now() - t0); if (!r.ok) throw new Error("HTTP " + r.status); const d = await r.json(); ids[i] = d.participant.id; ST.joined++; cell.classList.remove("send"); cell.classList.add("join"); } catch (e) { ST.joinErrors++; cell.classList.remove("send"); cell.classList.add("bad"); } if (i % 20 === 0) { refreshMetrics(); setProg(ST.joined / N); } }); refreshMetrics(); setProg(1); return ids; }
  function chooseAnswer(q, skill) { const good = Math.random() < skill; if (q.type === "multiple") { if (good) return q.correct.slice(); if (Math.random() < 0.5) return q.correct.slice(0, 1); return q.correct.slice(0, 1).concat(q.wrong.slice(0, 1)); } if (good) return [q.correct[0]]; return [q.wrong[(Math.random() * q.wrong.length) | 0]]; }
  async function runQuestion(q, qIndex, ids, skills) { const idxs = ids.map((p, i) => i).filter((i) => ids[i]); let ok = 0, err = 0, corr = 0, part = 0; const lat = []; await pool(idxs, cfg.CONC, async (i) => { const pid = ids[i]; const cell = UI.cells[i]; cell.className = "lt-cell send"; const ans = chooseAnswer(q, skills[i]); const elapsed = rint(800, TIME_LIMIT * 1000 - 1500); const t0 = performance.now(); try { const r = await fetch(`${cfg.BASE}/api/responses`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ participant_id: pid, question_id: q.id, answer_ids: ans, elapsed_ms: elapsed }) }); const ms = performance.now() - t0; lat.push(ms); ST.lat.resp.push(ms); const d = await r.json().catch(() => ({})); if (!r.ok) throw new Error("HTTP " + r.status); ok++; ST.responsesOk++; if (d.is_correct) { corr++; ST.correct++; cell.className = "lt-cell ok"; } else if (d.is_partial) { part++; ST.partial++; cell.className = "lt-cell part"; } else { cell.className = "lt-cell bad"; } } catch (e) { err++; ST.responsesErr++; cell.className = "lt-cell bad"; } if (ok % 20 === 0) refreshMetrics(); }); ST.perQuestion.push({ q: qIndex + 1, ok, err, correct: corr, partial: part, avgMs: avg(lat), p95Ms: pct(lat, 95) }); refreshMetrics(); }

  // NOUVEAU : classement intermédiaire après chaque question + suivi d'un joueur témoin.
  async function snapshot(qIndex) {
    const r = await fetch(`${cfg.SUPA}/rest/v1/participants?quiz_id=eq.${ST.quizId}&select=username,score&order=score.desc,username.asc`, { headers: { apikey: cfg.ANON, Authorization: `Bearer ${cfg.ANON}` } });
    const rows = await r.json();
    const leaderName = rows[0]?.username, leaderScore = rows[0]?.score ?? 0;
    const trackRank = ST.trackName ? rows.findIndex((p) => p.username === ST.trackName) + 1 : 0;
    const trackScore = ST.trackName ? (rows.find((p) => p.username === ST.trackName)?.score ?? 0) : 0;
    ST.snapshots.push({ q: qIndex + 1, total: rows.length, leaderName, leaderScore, trackRank, trackScore, top3: rows.slice(0, 3).map((p) => ({ u: p.username, s: p.score })) });
    // rendu
    UI.evo.innerHTML = ST.snapshots.map((s) => `<div class="row"><span class="q">Q${s.q}</span><span class="lead">🥇 ${s.leaderName} (${s.leaderScore})</span><span class="me">${ST.trackName} : #${s.trackRank}/${s.total}</span></div>`).join("");
    const last = ST.snapshots[ST.snapshots.length - 1];
    UI.track.style.display = "block";
    UI.track.innerHTML = `👤 Joueur témoin <b>${ST.trackName}</b> — après Q${last.q} : position <b>#${last.trackRank}</b> / ${last.total} · ${last.trackScore} pts`;
  }

  async function loadLeaderboard() { const r = await fetch(`${cfg.SUPA}/rest/v1/participants?quiz_id=eq.${ST.quizId}&select=username,score&order=score.desc&limit=10`, { headers: { apikey: cfg.ANON, Authorization: `Bearer ${cfg.ANON}` } }); const rows = await r.json(); ST.leaderboard = rows; const m = ["🥇", "🥈", "🥉"]; UI.lbwrap.innerHTML = `<table class="lt-lb">${rows.map((p, i) => `<tr><td class="lt-rk">${m[i] || (i + 1)}</td><td>${p.username}</td><td class="lt-sc">${p.score} pts</td></tr>`).join("")}</table>`; }
  const cleanup = () => fetch(`${cfg.SUPA}/rest/v1/quizzes?id=eq.${ST.quizId}`, { method: "DELETE", headers: svcH() });

  (async function run() {
    const C = Object.assign({ BASE: location.origin, N: 1000, CONC: 60, CLEANUP: true }, cfg); Object.assign(cfg, C);
    ST.startedAt = Date.now(); buildUI(cfg.N);
    ST.trackName = `Joueur_${String(Math.max(1, Math.floor(cfg.N / 2))).padStart(4, "0")}`; // joueur du milieu
    const skills = new Array(cfg.N).fill(0).map(() => 0.55 + Math.random() * 0.4);
    try {
      setPhase("création du quiz"); log("Création du quiz de test + 6 questions…", true);
      const { questions } = await createQuiz();
      log(`Quiz créé · code <b>${ST.code}</b> · ${questions.length} questions · « en attente »`);
      setPhase("inscriptions"); setProg(0); log(`Inscription de ${cfg.N} joueurs via /api/join (concurrence ${cfg.CONC})…`, true);
      const ids = await joinAll(cfg.N);
      log(`${ST.joined}/${cfg.N} inscrits · ${ST.joinErrors} échec(s) · moy ${avg(ST.lat.join)}ms · p95 ${pct(ST.lat.join, 95)}ms`);
      setPhase("démarrage live"); await patchQuiz({ status: "live", current_question_index: 0 }); log("Quiz passé EN DIRECT.", true);
      for (let qi = 0; qi < questions.length; qi++) {
        setPhase(`question ${qi + 1}/${questions.length}`);
        await patchQuiz({ status: "live", current_question_index: qi });
        log(`Question ${qi + 1} — « ${QDEF[qi].statement} » → envoi des réponses…`, true);
        await runQuestion(questions[qi], qi, ids, skills);
        await snapshot(qi); // classement intermédiaire APRÈS la question
        const r = ST.perQuestion[qi], s = ST.snapshots[qi];
        log(`Q${qi + 1}: ${r.ok} réponses · ${r.correct} ok · moy ${r.avgMs}ms / p95 ${r.p95Ms}ms — 🥇 ${s.leaderName} (${s.leaderScore}) · ${ST.trackName} #${s.trackRank}/${s.total}`);
        setProg((qi + 1) / questions.length);
        await sleep(400);
      }
      setPhase("fin du quiz"); await patchQuiz({ status: "finished" }); await loadLeaderboard(); log("Quiz terminé. Classement final chargé.", true);
      const allLat = ST.lat.join.concat(ST.lat.resp); const secs = (Date.now() - ST.startedAt) / 1000;
      ST.report = { users: cfg.N, joined: ST.joined, joinErrors: ST.joinErrors, responsesOk: ST.responsesOk, responsesErr: ST.responsesErr, totalRequests: ST.joined + ST.joinErrors + ST.responsesOk + ST.responsesErr, durationSec: Math.round(secs * 10) / 10, throughputRps: Math.round((ST.joined + ST.responsesOk + ST.joinErrors + ST.responsesErr) / secs), latency: { avgMs: avg(allLat), p50Ms: pct(allLat, 50), p95Ms: pct(allLat, 95), p99Ms: pct(allLat, 99), maxMs: Math.max(...allLat, 0) }, join: { avgMs: avg(ST.lat.join), p95Ms: pct(ST.lat.join, 95) }, resp: { avgMs: avg(ST.lat.resp), p95Ms: pct(ST.lat.resp, 95) }, perQuestion: ST.perQuestion, snapshots: ST.snapshots, leaderboardTop3: ST.leaderboard.slice(0, 3), errorRatePct: Math.round(((ST.joinErrors + ST.responsesErr) / Math.max(1, ST.joined + ST.joinErrors + ST.responsesOk + ST.responsesErr)) * 1000) / 10 };
      if (cfg.CLEANUP) { setPhase("nettoyage"); await cleanup(); log("Quiz de test supprimé (cascade).", true); }
      setPhase("✅ terminé"); ST.done = true; log("TEST TERMINÉ.", true);
    } catch (e) { ST.error = String(e); ST.done = true; setPhase("❌ erreur"); log("ERREUR: " + e, true); console.error(e); if (cfg.CLEANUP && ST.quizId) { try { await cleanup(); } catch (_) {} } }
  })();
})();

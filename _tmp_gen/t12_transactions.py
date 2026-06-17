# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle instruction marque le debut explicite d'une transaction ?", "BEGIN (ou START TRANSACTION)", "START", "OPEN TRANSACTION", "INIT"),
S("Quelle instruction valide de maniere definitive les modifications d'une transaction ?", "COMMIT", "SAVE", "VALIDATE", "CONFIRM"),
S("Quelle instruction annule toutes les modifications effectuees depuis le debut d'une transaction ?", "ROLLBACK", "CANCEL", "UNDO", "RESET"),
S("Que signifie le A de l'acronyme ACID pour les transactions ?", "Atomicite", "Autonomie", "Acces", "Agregation"),
S("Que signifie le C de l'acronyme ACID pour les transactions ?", "Coherence", "Concurrence", "Compression", "Cle"),
S("Que signifie le I de l'acronyme ACID pour les transactions ?", "Isolation", "Integration", "Index", "Identite"),
S("Que signifie le D de l'acronyme ACID pour les transactions ?", "Durabilite", "Dependance", "Distribution", "Donnees"),
S("Que garantit la propriete d'atomicite d'une transaction ?", "Toutes les operations de la transaction reussissent, ou aucune n'est appliquee", "Les operations s'executent toujours dans un ordre aleatoire", "Chaque requete est automatiquement validee", "Les donnees sont dupliquees sur plusieurs serveurs"),
S("Pourquoi grouper plusieurs instructions DML dans une seule transaction lors d'un virement bancaire ?", "Pour garantir que le debit et le credit soient appliques ensemble ou pas du tout", "Pour accelerer artificiellement la requete", "Pour eviter d'ecrire une clause WHERE", "Parce que SQL l'exige pour tout UPDATE"),
S("Que se passe-t-il aux modifications effectuees apres un ROLLBACK ?", "Elles sont annulees et la base revient a l'etat avant la transaction", "Elles sont validees definitivement", "Elles sont mises en attente jusqu'au prochain COMMIT", "Elles sont dupliquees dans une table d'archive"),
S("Quelle propriete ACID garantit que les transactions concurrentes ne s'influencent pas de maniere incoherente ?", "Isolation", "Atomicite", "Durabilite", "Coherence"),
]
ALL_MULTIPLE += [
M("Parmi les instructions suivantes, lesquelles sont liees a la gestion des transactions ?",
  ["BEGIN", "COMMIT", "ROLLBACK"], "SELECT", "CREATE INDEX"),
M("Quelles lettres et significations correspondent correctement a l'acronyme ACID ?",
  ["A pour Atomicite", "D pour Durabilite"], "C pour Cle primaire", "I pour Index"),
]
ALL_TF += [
TF("COMMIT rend les modifications d'une transaction permanentes et visibles pour les autres sessions.", True),
TF("ROLLBACK permet d'annuler les modifications non encore validees d'une transaction en cours.", True),
TF("Une transaction garantit qu'un ensemble d'operations est execute entierement ou pas du tout (atomicite).", True),
TF("Une fois qu'un COMMIT a ete execute, un ROLLBACK ultérieur peut encore annuler ces modifications validees.", False),
TF("La propriete de durabilite garantit que les modifications validees persistent meme apres une panne du systeme.", True),
]

print("t12:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t12.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)

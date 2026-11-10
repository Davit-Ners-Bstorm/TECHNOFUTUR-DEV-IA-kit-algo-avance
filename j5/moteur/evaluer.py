"""Mesurer la qualité du moteur et tester ses limites.

    uv run python -m j5.moteur.evaluer
"""
from j5.corpus import DOCUMENTS, QUESTION_SYNONYME, QUESTIONS
from outils.choix import charger

mot = charger("j5.moteur.moteur")
m = mot.Moteur(DOCUMENTS)

r = mot.evaluer(m, QUESTIONS, {"tous", "rh", "securite"})
print(f"Utilisateur avec tous les droits : precision@1 = {r['precision@1']:.0%}, rappel@3 = {r['rappel@3']:.0%}")

print("\nDétail :")
for q, attendus in QUESTIONS:
    res = m.rechercher(q, 3, {"tous", "rh", "securite"})
    ok = "✓" if res and res[0][0] in attendus else "✗"
    print(f"  {ok} {q:<62} → " + ", ".join(f"{i} ({s:.2f})" for i, s in res))

q, attendus = QUESTION_SYNONYME
res = m.rechercher(q, 3)
print(f"\nQuestion piège « {q} » (attendu {attendus}) → " + ", ".join(f"{i} ({s:.2f})" for i, s in res))
print("  Regardez le SCORE : même quand le bon document sort, peut-on s'y fier ?")

print("\nContrôle d'accès, utilisateur « tous » :")
for q in ("Grille des salaires par fonction", "Liste des comptes administrateurs"):
    print(f"  {q:<40} → " + ", ".join(i for i, _ in m.rechercher(q, 3, {"tous"})))

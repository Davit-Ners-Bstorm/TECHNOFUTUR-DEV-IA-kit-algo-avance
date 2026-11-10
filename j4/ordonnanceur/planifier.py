"""Planifier le pipeline de données fictif, puis provoquer un cycle.

    uv run python -m j4.ordonnanceur.planifier
"""
from j4.donnees_graphes import PIPELINE
from outils.choix import charger

od = charger("j4.ordonnanceur.ordonnanceur")
deps = {t: d for t, (_, d) in PIPELINE.items()}

print("Ordre d'exécution :")
for i, t in enumerate(od.tri_topologique(deps), 1):
    print(f"  {i:>2}. {t}")

print("\nVagues exécutables en parallèle :")
for i, vague in enumerate(od.niveaux(deps)):
    print(f"  vague {i} : {', '.join(vague)}")

duree, chemin = od.chemin_critique(PIPELINE)
print(f"\nDurée minimale : {duree} min (somme de toutes les tâches : {sum(d for d, _ in PIPELINE.values())} min)")
print("Chemin critique : " + " → ".join(chemin))

print("\nUn collègue ajoute : « nettoyer_clients dépend de rapport_qualite »")
deps_cyclique = dict(deps, nettoyer_clients=deps["nettoyer_clients"] + ["rapport_qualite"])
try:
    od.tri_topologique(deps_cyclique)
except od.CycleError as e:
    print(f"  Refusé, cycle détecté : {e}")

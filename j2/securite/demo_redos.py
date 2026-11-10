"""Démonstration : le temps de la regex vulnérable explose avec la longueur de l'entrée.

    uv run python -m j2.securite.demo_redos

Chaque ligne ajoute 2 caractères. Observez le ratio. N'allez pas au-delà de 26 !
"""
import time

from j2.versions_naives import nom_valide_regex

print(f"{'longueur':>9} | {'temps (s)':>10} | ratio")
precedent = None
for n in range(14, 27, 2):
    entree = "a" * n + "!"            # presque valide… mais le « ! » fait tout échouer
    debut = time.perf_counter()
    nom_valide_regex(entree)
    duree = time.perf_counter() - debut
    ratio = f"× {duree / precedent:.1f}" if precedent else "—"
    print(f"{n:>9} | {duree:>10.4f} | {ratio}")
    precedent = duree
print("\nÀ 40 caractères, il faudrait environ 18 heures (7 fois ×4). Un seul formulaire suffit à bloquer un serveur.")

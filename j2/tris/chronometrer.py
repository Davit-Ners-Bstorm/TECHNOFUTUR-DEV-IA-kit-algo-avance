"""Comparer vos tris entre eux et avec sorted().

    uv run python -m j2.tris.chronometrer

Questions pour la fiche :
  1. Quel ratio quand n double pour chaque tri ? Lequel est O(n²) ?
  2. tri_fusion et sorted() sont tous les deux O(n log n). Pourquoi sorted() est-il bien plus rapide ?
  3. Que devient sorted() sur une liste DÉJÀ triée ? Et tri_fusion ?
"""
import random

from j2 import versions_naives as naif
from outils.choix import charger
from outils.mesure import afficher_croissance, mesurer

t = charger("j2.tris.tris")
TAILLES = [2_000, 4_000, 8_000, 16_000]


def aleatoire(n):
    rng = random.Random(42)
    return ([rng.random() for _ in range(n)],)


def deja_triee(n):
    return (list(range(n)),)


for nom, f in [("tri_insertion (naïf)", naif.tri_insertion), ("tri_fusion", t.tri_fusion),
               ("tri_rapide", t.tri_rapide), ("sorted() — Timsort/Powersort", sorted)]:
    tailles = TAILLES[:3] if "insertion" in nom else TAILLES
    print(f"\n{nom} — liste aléatoire")
    try:
        afficher_croissance(mesurer(f, aleatoire, tailles))
    except NotImplementedError:
        print("  (pas encore écrit)")

print("\nsorted() — liste déjà triée")
afficher_croissance(mesurer(sorted, deja_triee, TAILLES))

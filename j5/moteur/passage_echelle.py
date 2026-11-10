"""Exact contre IVF : combien de rappel perdu pour combien de vitesse gagnée ?

    uv run python -m j5.moteur.passage_echelle
"""
import time

from j5.moteur.donnees_vecteurs import generer, questions
from outils.choix import charger

idx = charger("j5.moteur.index")
vecteurs = generer()
qs = questions(vecteurs)
print(f"{len(vecteurs)} vecteurs de dimension {len(vecteurs[0])}, {len(qs)} questions, k = 10")

exact = idx.IndexExact(vecteurs)
t = time.perf_counter()
verite = [exact.rechercher(q, 10) for q in qs]
t_exact = (time.perf_counter() - t) / len(qs)
print(f"\nExact : {t_exact * 1000:.1f} ms par question, rappel 100 %")

t = time.perf_counter()
ivf = idx.IndexIVF(vecteurs, n_listes=32, iterations=3)
print(f"Construction IVF (32 listes) : {time.perf_counter() - t:.1f} s")
print(f"\n{'sondes':>6} | {'ms / question':>13} | {'accélération':>12} | rappel@10")
for sondes in (1, 2, 4, 8):
    t = time.perf_counter()
    res = [ivf.rechercher(q, 10, sondes) for q in qs]
    duree = (time.perf_counter() - t) / len(qs)
    rappel = sum(idx.rappel_a_k(r, v) for r, v in zip(res, verite)) / len(qs)
    print(f"{sondes:>6} | {duree * 1000:>13.1f} | {t_exact / duree:>11.1f}× | {rappel:.1%}")

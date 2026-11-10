"""Démo formateur — LE cliffhanger : la même similarité cosinus, en boucles Python puis avec NumPy.

    uv run python -m j5.demos.vers_numpy

NumPy fait partie du module suivant : ici, on regarde seulement le chronomètre.
"""
import math
import time

import numpy as np

from j5.moteur.donnees_vecteurs import generer

vecteurs = generer(n=50_000, dim=64)
q = vecteurs[0]

t = time.perf_counter()
scores = [sum(a * b for a, b in zip(q, v)) / (math.sqrt(sum(a * a for a in q)) * math.sqrt(sum(b * b for b in v)))
          for v in vecteurs]
t_python = time.perf_counter() - t

M = np.array(vecteurs)
qv = np.array(q)
t = time.perf_counter()
scores_np = (M @ qv) / (np.linalg.norm(M, axis=1) * np.linalg.norm(qv))
t_numpy = time.perf_counter() - t

print(f"Boucles Python : {t_python * 1000:8.1f} ms")
print(f"NumPy          : {t_numpy * 1000:8.1f} ms   → {t_python / t_numpy:.0f} fois plus rapide")
print(f"Même résultat ? {np.allclose(scores, scores_np)}")

# Les vecteurs sont déjà normalisés à l'indexation : le cosinus devient un simple produit.
t = time.perf_counter()
scores_np2 = M @ qv
t_numpy2 = time.perf_counter() - t
print(f"NumPy, vecteurs normalisés une fois pour toutes : {t_numpy2 * 1000:.1f} ms "
      f"→ {t_python / t_numpy2:.0f} fois plus rapide que les boucles")
print("\nPourquoi ? La boucle tourne en C, sur des nombres rangés côte à côte en mémoire,")
print("avec les instructions vectorielles du processeur. Rendez-vous au module NumPy.")

"""Démo — Sac à dos : de la force brute (2^n) à la programmation dynamique (n × capacité).

Contexte IA : choisir quels documents mettre dans le contexte d'un LLM. Chaque document a
un « poids » (ses tokens) et une « valeur » (sa pertinence) ; la fenêtre de contexte est la capacité.

    uv run python -m j3.demos.sac_a_dos
"""
import random
import time

from j3.versions_naives import sac_a_dos_force_brute


def sac_a_dos_dp(objets, capacite):
    """meilleur[c] = meilleure valeur avec une capacité c, en n'utilisant que les objets vus."""
    meilleur = [0] * (capacite + 1)
    for poids, valeur in objets:
        for c in range(capacite, poids - 1, -1):     # à rebours : chaque objet une seule fois
            meilleur[c] = max(meilleur[c], meilleur[c - poids] + valeur)
    return meilleur[capacite]


rng = random.Random(3)
print(f"{'n':>3} | {'force brute':>11} | {'DP':>8} | même résultat")
for n in (10, 18, 24, 26):
    objets = [(rng.randint(100, 2_000), rng.randint(1, 100)) for _ in range(n)]
    capacite = 8_000                                   # « 8 000 tokens »
    t0 = time.perf_counter(); fb = sac_a_dos_force_brute(objets, capacite)
    t1 = time.perf_counter(); dp = sac_a_dos_dp(objets, capacite)
    t2 = time.perf_counter()
    print(f"{n:>3} | {t1 - t0:>10.3f}s | {t2 - t1:>7.3f}s | {fb == dp}")

objets = [(rng.randint(100, 2_000), rng.randint(1, 100)) for _ in range(200)]
t = time.perf_counter(); sac_a_dos_dp(objets, 8_000)
print(f"\n200 documents, DP : {time.perf_counter() - t:.2f} s. Force brute : 2^200 combinaisons, jamais.")

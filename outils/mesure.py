"""Petits outils de mesure, à utiliser pendant les exercices.

Idée clé : on ne devine pas la complexité, on la MESURE.
On double la taille de l'entrée et on regarde comment le temps évolue :
    temps × 2  → croissance linéaire, O(n)
    temps × 4  → croissance quadratique, O(n²)
    temps ≈ ×1 → constant ou logarithmique, O(1) / O(log n)
"""
import timeit
import tracemalloc
from collections.abc import Callable


def mesurer(fonction: Callable, fabriquer_entree: Callable[[int], tuple],
            tailles: list[int], repetitions: int = 3) -> list[tuple[int, float]]:
    """Retourne [(n, meilleur temps en secondes), ...].

    `fabriquer_entree(n)` doit renvoyer le TUPLE d'arguments à passer à `fonction`.
    La construction de l'entrée n'est pas chronométrée.
    """
    resultats = []
    for n in tailles:
        args = fabriquer_entree(n)
        temps = min(timeit.repeat(lambda: fonction(*args), number=1, repeat=repetitions))
        resultats.append((n, temps))
    return resultats


def verdict(ratio: float) -> str:
    if ratio < 1.5:
        return "≈ O(1) ou O(log n)"
    if ratio < 2.6:
        return "≈ O(n) ou O(n log n)"
    if ratio < 5:
        return "≈ O(n²)"
    return "pire que O(n²) !"


def afficher_croissance(resultats: list[tuple[int, float]]) -> None:
    """Affiche un tableau n / temps / ratio entre deux tailles successives.

    Pour que le ratio ait un sens, utiliser des tailles qui DOUBLENT : 1000, 2000, 4000…
    """
    print(f"{'n':>10} | {'temps (ms)':>12} | {'ratio':>6} | verdict")
    print("-" * 52)
    precedent = None
    for n, t in resultats:
        if precedent:
            ratio = t / precedent if precedent > 0 else float("inf")
            print(f"{n:>10} | {t * 1000:>12.3f} | {ratio:>6.2f} | {verdict(ratio)}")
        else:
            print(f"{n:>10} | {t * 1000:>12.3f} | {'—':>6} |")
        precedent = t


def pic_memoire(fonction: Callable, *args) -> int:
    """Pic de mémoire (en octets) alloué pendant l'appel de la fonction."""
    tracemalloc.start()
    try:
        fonction(*args)
        _, pic = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return pic

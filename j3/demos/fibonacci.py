"""Démo — Le même calcul fait des millions de fois, puis une seule.

    uv run python -m j3.demos.fibonacci
"""
import time
from functools import cache

appels = 0


def fib_naif(n):
    global appels
    appels += 1
    return n if n < 2 else fib_naif(n - 1) + fib_naif(n - 2)


@cache
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)


def fib_tableau(n):
    """Programmation dynamique « de bas en haut » : pas de récursion, mémoire O(1)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(f"{'n':>3} | {'appels fib_naif':>16} | {'temps naïf':>10}")
for n in (10, 20, 25, 30):
    appels = 0
    debut = time.perf_counter()
    fib_naif(n)
    print(f"{n:>3} | {appels:>16,} | {time.perf_counter() - debut:>9.3f}s".replace(",", " "))

debut = time.perf_counter()
fib_memo(500)
print(f"\nfib_memo(500)    : {time.perf_counter() - debut:.5f} s, {fib_memo.cache_info().currsize} valeurs en cache")
debut = time.perf_counter()
x = fib_tableau(10_000)
print(f"fib_tableau(10 000) : {time.perf_counter() - debut:.5f} s, {len(str(x))} chiffres")

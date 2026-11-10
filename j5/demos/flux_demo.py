"""Démo formateur — Bloom filter et HyperLogLog : des réponses approchées, une mémoire minuscule.

    uv run python -m j5.demos.flux_demo
"""
import hashlib
import math
import sys


def h64(x: str) -> int:
    return int.from_bytes(hashlib.blake2b(x.encode(), digest_size=8).digest(), "big")


class HyperLogLog:
    """Compter les éléments DISTINCTS d'un flux avec 2^p registres de quelques bits.
    Idée : dans des hachages aléatoires, voir un long préfixe de zéros est rare ; le plus long
    préfixe observé renseigne sur le nombre d'éléments différents vus."""

    def __init__(self, p: int = 12):
        self.p, self.m = p, 1 << p
        self.registres = bytearray(self.m)

    def ajouter(self, x: str):
        h = h64(x)
        j = h >> (64 - self.p)                         # les p premiers bits choisissent le registre
        reste = h & ((1 << (64 - self.p)) - 1)
        rang = (64 - self.p) - reste.bit_length() + 1  # position du premier 1
        self.registres[j] = max(self.registres[j], rang)

    def estimer(self) -> float:
        alpha = 0.7213 / (1 + 1.079 / self.m)
        e = alpha * self.m * self.m / sum(2.0 ** -r for r in self.registres)
        vides = self.registres.count(0)
        if e <= 2.5 * self.m and vides:                # correction pour les petits nombres
            e = self.m * math.log(self.m / vides)
        return e


print("HyperLogLog — combien de visiteurs DIFFÉRENTS ?")
for n in (1_000, 100_000, 1_000_000):
    hll, exact = HyperLogLog(12), set()
    for i in range(n):
        x = f"visiteur-{i % (n // 2)}"                 # chaque visiteur vient deux fois
        hll.ajouter(x)
        exact.add(x)
    est = hll.estimer()
    print(f"  {n:>9} visites : {len(exact):>7} distincts, estimation {est:>9.0f} "
          f"(erreur {abs(est - len(exact)) / len(exact):.1%}), "
          f"mémoire HLL {len(hll.registres) / 1024:.0f} Kio contre set ≈ {sys.getsizeof(exact) / 1024 / 1024:.0f} Mio (sans les chaînes)")

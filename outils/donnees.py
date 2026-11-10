"""Jeux de données fictifs et reproductibles pour les exercices.

Aucune donnée réelle : noms et e-mails sont inventés, domaine example.org.
La graine fixe garantit que tout le groupe travaille sur les mêmes données.
"""
import random

PRENOMS = ["alice", "bruno", "chloe", "david", "emma", "farid", "gaelle", "hugo",
           "ines", "jules", "karim", "lea", "malik", "nora", "oscar", "pauline"]
NOMS = ["dupont", "janssens", "peeters", "maes", "lambert", "dubois", "willems",
        "claes", "goossens", "mertens", "leroy", "simon", "laurent", "renard"]
PRODUITS = [f"P{i:04d}" for i in range(2_000)]


def emails(n: int, taux_doublons: float = 0.05, graine: int = 42) -> list[str]:
    """n adresses e-mail fictives, dont environ `taux_doublons` en double."""
    rng = random.Random(graine)
    uniques = [f"{rng.choice(PRENOMS)}.{rng.choice(NOMS)}{i}@example.org" for i in range(n)]
    for _ in range(int(n * taux_doublons)):
        uniques[rng.randrange(n)] = uniques[rng.randrange(n)]
    return uniques


def nombres(n: int, maxi: int = 1_000_000, graine: int = 42) -> list[int]:
    rng = random.Random(graine)
    return [rng.randint(-maxi, maxi) for _ in range(n)]


def ventes(n: int, graine: int = 42) -> list[tuple[str, int]]:
    """n lignes de vente (code produit, quantité)."""
    rng = random.Random(graine)
    return [(rng.choice(PRODUITS), rng.randint(1, 20)) for _ in range(n)]


def mesures_capteur(n: int, graine: int = 42) -> list[float]:
    rng = random.Random(graine)
    return [round(20 + rng.gauss(0, 3), 2) for _ in range(n)]


def prix_tries(n: int, graine: int = 42) -> list[float]:
    rng = random.Random(graine)
    return sorted(round(rng.uniform(1, 1_000), 2) for _ in range(n))

"""Vecteurs denses synthétiques regroupés en « thèmes », comme des embeddings de documents."""
import math
import random


def _normaliser(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


def generer(n: int = 10_000, dim: int = 32, n_themes: int = 40, sous_themes: int = 8,
            bruit_theme: float = 0.6, bruit_doc: float = 0.15, graine: int = 5):
    """Thèmes → sous-thèmes → documents : une structure à plusieurs niveaux, comme de vrais embeddings
    (« sécurité » → « mots de passe » → un document précis)."""
    rng = random.Random(graine)
    themes = [_normaliser([rng.gauss(0, 1) for _ in range(dim)]) for _ in range(n_themes)]
    sous = [_normaliser([x + rng.gauss(0, bruit_theme) for x in t]) for t in themes for _ in range(sous_themes)]
    return [_normaliser([x + rng.gauss(0, bruit_doc) for x in rng.choice(sous)]) for _ in range(n)]


def questions(vecteurs, n: int = 30, bruit: float = 0.05, graine: int = 9):
    """Questions proches de vecteurs existants (une question ressemble à des documents)."""
    rng = random.Random(graine)
    return [_normaliser([x + rng.gauss(0, bruit) for x in rng.choice(vecteurs)]) for _ in range(n)]

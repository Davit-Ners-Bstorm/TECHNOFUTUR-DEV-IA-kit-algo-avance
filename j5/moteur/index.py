"""MINI-PROJET — Étape 3 : passer à l'échelle avec un index approximatif (IVF).

Avec 30 documents, comparer la question à tous est instantané. Avec 10 millions de vecteurs
d'embedding, non. Les bases vectorielles utilisent des index APPROXIMATIFS : un peu de rappel
perdu contre beaucoup de vitesse. On construit le plus simple : IVF (inverted file).

  - Construction : regrouper les vecteurs en n_listes groupes avec quelques tours de k-means ;
    chaque groupe a un centre (centroïde).
  - Recherche : comparer la question aux centroïdes, ne fouiller que les n_sondes groupes
    les plus proches, puis faire un top-k exact sur leurs vecteurs.

Vecteurs denses = listes de float de même dimension, NORMALISÉS (le produit scalaire = cosinus).

    uv run pytest j5/moteur
    uv run python -m j5.moteur.passage_echelle
"""
import heapq    # noqa: F401
import random   # noqa: F401


def produit(u: list[float], v: list[float]) -> float:
    """Produit scalaire. Fourni."""
    return sum(a * b for a, b in zip(u, v))


class IndexExact:
    """k plus proches voisins par force brute : O(n × dimension) par question. C'est l'oracle."""

    def __init__(self, vecteurs: list[list[float]]):
        self.vecteurs = vecteurs

    def rechercher(self, q: list[float], k: int) -> list[int]:
        """Indices des k vecteurs de plus grand produit scalaire avec q, du plus proche au moins proche."""
        raise NotImplementedError


class IndexIVF:
    def __init__(self, vecteurs: list[list[float]], n_listes: int = 64, iterations: int = 5, graine: int = 0):
        """k-means simplifié :
          1. centroïdes = n_listes vecteurs tirés au hasard (random.Random(graine)) ;
          2. répéter `iterations` fois : affecter chaque vecteur au centroïde de plus grand produit,
             puis recalculer chaque centroïde comme la moyenne de ses vecteurs, renormalisée ;
          3. garder les listes : centroïde → indices de ses vecteurs.
        """
        raise NotImplementedError

    def rechercher(self, q: list[float], k: int, n_sondes: int = 4) -> list[int]:
        """Top-k exact, mais seulement parmi les vecteurs des n_sondes listes les plus proches de q."""
        raise NotImplementedError


def rappel_a_k(trouves: list[int], exacts: list[int]) -> float:
    """Part des vrais k plus proches voisins retrouvés par l'index approximatif. Fourni."""
    return len(set(trouves) & set(exacts)) / len(exacts) if exacts else 1.0

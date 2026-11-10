"""LAB J1 — Le bon choix de structure de données.

Pour chaque fonction :
  1. lis la version lente dans versions_naives.py ;
  2. mesure-la avec outils/mesure.py pour confirmer sa complexité ;
  3. écris ici une version rapide, avec la structure indiquée ;
  4. lance les tests :  uv run pytest j1/lab

Les signatures et le comportement attendu sont IDENTIQUES à versions_naives.py.
Chaque fonction a un budget de temps sur une grande entrée (tests marqués « perf »).
"""
from collections import deque          # noqa: F401  (utile pour moyenne_glissante)
import bisect                          # noqa: F401  (utile pour compter_dans_tranche)
import heapq                           # noqa: F401  (utile pour top_k)


def doublons(emails: list[str]) -> list[str]:
    """Objectif : O(n). Indice : un `set` répond à « déjà vu ? » en temps constant."""
    raise NotImplementedError


def paires_somme(nombres: list[int], cible: int) -> bool:
    """Objectif : O(n), un seul parcours. Indice : pour chaque x, que cherches-tu ?"""
    raise NotImplementedError


def top_k(ventes: list[tuple[str, int]], k: int) -> list[tuple[str, int]]:
    """Objectif : O(n + m log k) avec m produits distincts.

    Indices : un `dict` pour les totaux, puis `heapq.nsmallest` avec une clé bien choisie.
    """
    raise NotImplementedError


def moyenne_glissante(valeurs: list[float], fenetre: int) -> list[float]:
    """Objectif : O(n). Indice : une somme courante ; on ajoute l'entrant, on retire le sortant.

    Bonus : utilise une `deque` pour la fenêtre, comme si les valeurs arrivaient en flux.
    """
    raise NotImplementedError


def compter_dans_tranche(prix_tries: list[float], bas: float, haut: float) -> int:
    """Objectif : O(log n). Indice : `bisect_left` et `bisect_right`."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# BONUS — mémoïsation avec frozendict (Python 3.15)
# ---------------------------------------------------------------------------
APPELS = {"tarif_lent": 0}


def tarif_lent(options: dict) -> float:
    """Calcul « coûteux » (imagine un appel réseau ou un modèle). Ne pas modifier."""
    APPELS["tarif_lent"] += 1
    base = 100.0
    if options.get("premium"):
        base *= 1.5
    return round(base * (1 - options.get("remise", 0) / 100), 2)


def tarif(options: dict) -> float:
    """Même résultat que tarif_lent, mais chaque combinaison d'options n'est calculée qu'une fois.

    Piège : `functools.cache` exige des arguments HACHABLES, et un dict ne l'est pas.
    Indice : convertis `options` en `frozendict` avant de passer par la fonction en cache.
    """
    raise NotImplementedError

"""EXERCICE 1 — Recherche et tris (exercice guidé).

Règle du jeu : on n'utilise ni sorted(), ni list.sort(), ni bisect, ni heapq.nlargest.
On les réécrit pour comprendre ce qu'ils font. (heapq.heappush / heappop sont autorisés.)

    uv run pytest j2/tris
    uv run python -m j2.tris.chronometrer     ← compare vos tris à sorted()
"""
import heapq      # noqa: F401
import random     # noqa: F401


def recherche_dichotomique(lst: list, x) -> int:
    """Indice de la PREMIÈRE occurrence de x dans une liste TRIÉE, ou -1. Objectif : O(log n).

    Piège classique : avec des doublons, s'arrêter au premier x trouvé ne donne pas
    forcément la première occurrence.
    """
    raise NotImplementedError


def tri_fusion(lst: list) -> list:
    """Renvoie une NOUVELLE liste triée. O(n log n), STABLE.

    Stable : deux éléments égaux gardent leur ordre d'origine.
    Indice : couper en deux, trier chaque moitié, fusionner. Dans la fusion, en cas
    d'égalité, prendre d'abord l'élément de la moitié GAUCHE.
    """
    raise NotImplementedError


def tri_rapide(lst: list) -> list:
    """Renvoie une NOUVELLE liste triée. O(n log n) en moyenne.

    Deux pièges testés :
      - une liste DÉJÀ triée ne doit pas faire exploser le temps → pivot aléatoire ;
      - une liste avec beaucoup de DOUBLONS non plus → partition en trois
        (plus petits / égaux / plus grands).
    """
    raise NotImplementedError


def top_k(valeurs, k: int) -> list:
    """Les k plus grandes valeurs, de la plus grande à la plus petite. O(n log k).

    Interdit : trier toutes les valeurs. Indice : garder un tas de taille k
    qui contient les k meilleures vues jusqu'ici (heappush / heappushpop).
    `valeurs` peut être un itérateur : on ne peut le parcourir qu'une fois.
    """
    raise NotImplementedError


def fusion_k_listes(listes: list[list]) -> list:
    """BONUS — fusionne k listes déjà triées en une liste triée. O(n log k).

    C'est le cœur du TRI EXTERNE : on trie des morceaux qui tiennent en mémoire,
    puis on les fusionne en ne gardant qu'un élément par morceau dans un tas.
    Interdit : heapq.merge (c'est lui qu'on réécrit).
    """
    raise NotImplementedError

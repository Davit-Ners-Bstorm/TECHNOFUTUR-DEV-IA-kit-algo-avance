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
    low = 0
    high = len(lst) - 1

    pos = -1

    while low <= high:
        middle = (low + high) // 2

        if lst[middle] == x:
            pos = middle
            high = middle - 1
        
        elif lst[middle] < x:
            low = middle + 1
            
        else:
            high = middle - 1

    return pos

def fusion(gauche, droite):
    resultat = []
    i = 0
    j = 0

    while i < len(gauche) and j < len(droite):
        if gauche[i] > droite[j]:
            resultat.append(droite[j])
            j += 1
        else:
            resultat.append(gauche[i])
            i += 1

    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])

    return resultat


def tri_fusion(lst: list) -> list:
    """Renvoie une NOUVELLE liste triée. O(n log n), STABLE.

    Stable : deux éléments égaux gardent leur ordre d'origine.
    Indice : couper en deux, trier chaque moitié, fusionner. Dans la fusion, en cas
    d'égalité, prendre d'abord l'élément de la moitié GAUCHE.
    """

    if len(lst) <= 1:
        # print(f"############### DERNIERE RECURSION ({lst})")
        return lst

    mid = len(lst) // 2

    # print(f"***** DIVISION gauche droite de {lst} = {lst[:mid]} et {lst[mid:]}")
    
    gauche = tri_fusion(lst[:mid])
    droite = tri_fusion(lst[mid:])

    # print(gauche, droite)

    return fusion(gauche, droite)

# print(tri_fusion([4, 5, 8, 2]))


import random

def tri_rapide(lst: list) -> list:
    """Renvoie une NOUVELLE liste triée. O(n log n) en moyenne.
    [5, 2, 6, 8, 4]


    Deux pièges testés :
      - une liste DÉJÀ triée ne doit pas faire exploser le temps → pivot aléatoire ;
      - une liste avec beaucoup de DOUBLONS non plus → partition en trois
        (plus petits / égaux / plus grands).
    """

    if len(lst) <= 1:
        return lst

    pivot = random.choice(lst)

    petits = []
    egaux = []
    grands = []

    for elem in lst:
        if elem < pivot:
            petits.append(elem)
        elif elem > pivot:
            grands.append(elem)
        else:
            egaux.append(elem)
    
    return tri_rapide(petits) + egaux + tri_rapide(grands)

# print(tri_rapide([8, 9, 5, 26, 1, 3, 4, 98, 65, 13]))

import heapq

def top_k(valeurs, k: int) -> list:
    # [1, 5, 3, 8, 9, 46, 85, 2] - 3
    # [5, 4, 6, 8, 16]
    """Les k plus grandes valeurs, de la plus grande à la plus petite. O(n log k).

    Interdit : trier toutes les valeurs. Indice : garder un tas de taille k
    qui contient les k meilleures vues jusqu'ici (heappush / heappushpop).
    `valeurs` peut être un itérateur : on ne peut le parcourir qu'une fois.
    """

    if k < 1:
        return []

    resultats = []

    for x in valeurs:
        if len(resultats) < k:
            heapq.heappush(resultats, x)
        else:
            heapq.heappushpop(resultats, x)

    sorted_resultat = []

    while resultats:
        sorted_resultat.append(heapq.heappop(resultats))

    return sorted_resultat[::-1]

# print(top_k([5, 8, 9, 13, 65, 45, 2, 1, 3, 54, 65, 98], 10))


def fusion_k_listes(listes: list[list]) -> list:
    """BONUS — fusionne k listes déjà triées en une liste triée. O(n log k).

    C'est le cœur du TRI EXTERNE : on trie des morceaux qui tiennent en mémoire,
    puis on les fusionne en ne gardant qu'un élément par morceau dans un tas.
    Interdit : heapq.merge (c'est lui qu'on réécrit).
    """
    raise NotImplementedError

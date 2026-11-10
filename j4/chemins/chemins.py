"""LAB J4 (partie 2) — Plus courts chemins pondérés, et union-find en bonus.

Graphe pondéré : {sommet: [(voisin, coût), ...]}, coûts positifs (donnees_graphes.carte_ponderee()).
Grille : liste de chaînes, '#' = mur, '.' = libre (donnees_graphes.grille()).

    uv run pytest j4/chemins
    uv run python -m j4.chemins.comparer     ← Dijkstra contre A* sur le labyrinthe
"""
import heapq   # noqa: F401


def dijkstra(graphe: dict, depart, arrivee) -> tuple[float, list] | None:
    """(coût total, chemin) du plus court chemin pondéré, ou None si inatteignable.

    File de priorité (heapq) de (coût depuis le départ, sommet). On sort toujours le sommet le
    plus proche ; quand on le sort, son coût est DÉFINITIF. Retenir le parent pour reconstruire.
    Piège : un sommet peut être dans le tas plusieurs fois ; ignorer les entrées périmées.
    """
    raise NotImplementedError


def voisins_grille(grille: list[str], case: tuple[int, int]):
    """Cases libres voisines (haut, bas, gauche, droite) de case = (ligne, colonne). Fourni."""
    l, c = case
    for dl, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nl, nc = l + dl, c + dc
        if 0 <= nl < len(grille) and 0 <= nc < len(grille[0]) and grille[nl][nc] != "#":
            yield (nl, nc)


def a_etoile(grille: list[str], depart: tuple[int, int], arrivee: tuple[int, int],
             heuristique: bool = True) -> tuple[int, int] | None:
    """(longueur du plus court chemin, nombre de cases EXPLORÉES), ou None si pas de chemin.

    Comme Dijkstra (chaque pas coûte 1), mais la priorité est coût_connu + estimation_restante.
    Estimation : distance de Manhattan jusqu'à l'arrivée. Avec heuristique=False, l'estimation
    vaut 0 : c'est exactement Dijkstra. Comparez le nombre de cases explorées.
    """
    raise NotImplementedError


def grouper(paires: list[tuple], elements: list | None = None) -> list[set]:
    """BONUS — Union-find : regrouper des éléments reliés par des paires.

    Application directe du J3 : les paires de doublons (a, b), (b, c) forment UN client {a, b, c}.
    Chaque élément a un « parent » ; trouver(x) remonte jusqu'au représentant (compression de chemin) ;
    unir(a, b) rattache un représentant à l'autre. Les éléments sans paire forment un groupe seuls.
    """
    raise NotImplementedError

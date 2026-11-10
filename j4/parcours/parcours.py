"""EXERCICE 1 — Parcourir un réseau de dépendances (exercice guidé).

Un graphe est représenté par un dict d'adjacence : sommet → liste de voisins.
Dans j4/donnees_graphes.DEPENDANCES, « A: [B, C] » veut dire « A dépend de B et de C ».

Scénario réel (Cyber Resilience Act, SBOM) : une faille est publiée dans « crypto-base ».
Quels paquets de notre parc sont touchés, directement ou indirectement ?

Règle : pas de récursion pour les parcours (une pile ou une file explicite), pas de networkx.

    uv run pytest j4/parcours
"""
from collections import deque   # noqa: F401


def inverser(graphe: dict[str, list[str]]) -> dict[str, list[str]]:
    """Graphe des arcs inversés : si A → B, alors B → A dans le résultat.
    Tous les sommets du graphe d'origine doivent être des clés du résultat."""
    raise NotImplementedError


def atteignables(graphe: dict, depart) -> set:
    """Parcours en PROFONDEUR (DFS) avec une pile : tous les sommets atteignables depuis depart,
    depart compris. Doit supporter les cycles et 100 000 sommets."""
    raise NotImplementedError


def impactes(dependances: dict[str, list[str]], paquet_vulnerable: str) -> set[str]:
    """Paquets qui dépendent, directement ou non, du paquet vulnérable (lui-même exclu).
    Indice : qui « remonte » vers le paquet vulnérable ? Inversez, puis parcourez."""
    raise NotImplementedError


def distances(graphe: dict, depart) -> dict:
    """Parcours en LARGEUR (BFS) avec une file (deque) : sommet → nombre d'arcs depuis depart.
    Les sommets non atteignables n'apparaissent pas."""
    raise NotImplementedError


def chemin_le_plus_court(graphe: dict, a, b) -> list | None:
    """Chemin avec le moins d'arcs de a à b (liste de sommets, a et b compris), ou None.
    Indice : pendant le BFS, retenez le parent de chaque sommet découvert, puis remontez depuis b."""
    raise NotImplementedError


def composantes(graphe: dict) -> list[set]:
    """Composantes connexes d'un graphe NON orienté : groupes de sommets reliés entre eux."""
    raise NotImplementedError

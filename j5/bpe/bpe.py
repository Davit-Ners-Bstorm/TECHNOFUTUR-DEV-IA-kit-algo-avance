"""EXERCICE 1 — La tokenisation BPE, à la main (exercice guidé, 30 min).

Un LLM ne lit pas des mots mais des « tokens ». BPE (Byte Pair Encoding) apprend ces tokens :
  1. on part des caractères ;
  2. on compte toutes les paires de symboles voisins dans le corpus ;
  3. on FUSIONNE la paire la plus fréquente en un nouveau symbole ;
  4. on recommence n fois. La liste des fusions EST le vocabulaire appris.

Représentation : un mot = un tuple de symboles. ("b", "a", "s", "</w>") ; "</w>" marque la fin du mot.
Le corpus = un dict {mot_en_symboles: nombre d'occurrences}.

    uv run pytest j5/bpe
"""
from collections import Counter   # noqa: F401

FIN = "</w>"


def preparer(texte: str) -> dict[tuple[str, ...], int]:
    """'bas bas basse' → {('b','a','s','</w>'): 2, ('b','a','s','s','e','</w>'): 1}. Fourni."""
    compte: dict[tuple[str, ...], int] = {}
    for mot in texte.lower().split():
        cle = tuple(mot) + (FIN,)
        compte[cle] = compte.get(cle, 0) + 1
    return compte


def compter_paires(corpus: dict[tuple[str, ...], int]) -> dict[tuple[str, str], int]:
    """Fréquence de chaque paire de symboles VOISINS, pondérée par le nombre d'occurrences du mot."""
    raise NotImplementedError


def fusionner(corpus: dict[tuple[str, ...], int], paire: tuple[str, str]) -> dict[tuple[str, ...], int]:
    """Nouveau corpus où chaque occurrence de la paire (a, b) est remplacée par le symbole a+b.
    Parcourir chaque mot de gauche à droite ; après une fusion, sauter le symbole fusionné."""
    raise NotImplementedError


def entrainer(texte: str, n_fusions: int) -> list[tuple[str, str]]:
    """Les fusions apprises, dans l'ordre. À égalité de fréquence, prendre la plus petite paire
    dans l'ordre alphabétique (pour que le résultat soit reproductible). S'arrêter s'il n'y a plus de paire."""
    raise NotImplementedError


def tokeniser(mot: str, fusions: list[tuple[str, str]]) -> list[str]:
    """Découper un mot (même jamais vu) en appliquant les fusions DANS L'ORDRE où elles ont été apprises."""
    raise NotImplementedError

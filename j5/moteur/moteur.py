"""MINI-PROJET — Étape 2 : le moteur de recherche (le « R » de RAG).

Exigences :
  - indexer les documents (titre + texte) une seule fois, à la construction ;
  - rechercher(question, k, groupes) → les k documents les plus proches, (id, score) par score décroissant,
    en ignorant les scores nuls ;
  - SÉCURITÉ : un document n'est candidat que si l'utilisateur a au moins un de ses groupes.
    Le filtre s'applique AVANT le classement : un document interdit ne doit ni sortir, ni
    prendre la place d'un document autorisé ;
  - SÉCURITÉ : une question de plus de 500 caractères est refusée (ValueError) ;
  - top-k avec un tas (J2), pas un tri complet.

    uv run pytest j5/moteur
    uv run python -m j5.moteur.evaluer
"""
import heapq   # noqa: F401

from outils.choix import charger

v = charger("j5.moteur.vecteurs")

LONGUEUR_MAX_QUESTION = 500


class Moteur:
    def __init__(self, documents: list[tuple[str, str, str, set[str]]]):
        """documents = [(id, titre, texte, groupes), ...]"""
        raise NotImplementedError

    def rechercher(self, question: str, k: int = 3, groupes: set[str] = frozenset({"tous"})) -> list[tuple[str, float]]:
        raise NotImplementedError


# ------------------------------------------------------------ fourni
def evaluer(moteur: Moteur, questions, groupes: set[str]) -> dict[str, float]:
    """precision@1 : le 1er résultat est-il pertinent ?  rappel@3 : part des documents attendus dans le top 3."""
    p1 = r3 = 0.0
    for q, attendus in questions:
        res = [i for i, _ in moteur.rechercher(q, 3, groupes)]
        p1 += bool(res) and res[0] in attendus
        r3 += len(set(res) & attendus) / len(attendus)
    return {"precision@1": p1 / len(questions), "rappel@3": r3 / len(questions)}

"""MINI-PROJET — Étape 1 : transformer un texte en vecteur, et mesurer la ressemblance.

On fabrique des vecteurs LEXICAUX (TF-IDF sur des mots et des trigrammes de lettres).
Un vrai RAG utilise un modèle d'embedding qui capte le SENS (synonymes compris), mais
les algorithmes qui suivent (cosinus, k plus proches voisins, index) sont exactement les mêmes.

Un vecteur creux est un dict {caractéristique: poids} : seules les valeurs non nulles sont stockées.
"""
import math        # noqa: F401
import unicodedata  # noqa: F401

MOTS_VIDES = {"le", "la", "les", "un", "une", "des", "de", "du", "d", "l", "et", "ou", "a", "au", "aux",
              "en", "dans", "par", "pour", "sur", "avec", "ne", "pas", "que", "qui", "quoi", "est", "sont",
              "je", "j", "me", "m", "mon", "ma", "mes", "on", "il", "elle", "se", "s", "ses", "son", "sa",
              "votre", "vos", "vous", "ce", "cette", "y", "n", "puis", "comment", "faire", "ai"}


def tokens(texte: str) -> list[str]:
    """Minuscules, sans accents ; découper sur tout ce qui n'est pas lettre ou chiffre ;
    retirer les mots vides et les mots d'une seule lettre.
    'J'ai oublié mon Mot-de-passe !' → ['oublie', 'mot', 'passe']
    """
    raise NotImplementedError


def caracteristiques(texte: str) -> list[str]:
    """Les mots de tokens(texte), PLUS les trigrammes de lettres de chaque mot entouré de '#'.
    'conge' → 'conge', '#co', 'con', 'ong', 'nge', 'ge#'.
    Les trigrammes rapprochent « congé » et « congés », « volé » et « vol »."""
    raise NotImplementedError


def idf(corpus: list[list[str]]) -> dict[str, float]:
    """Pour chaque caractéristique : log((N + 1) / (df + 1)) + 1, où df = nombre de documents qui la contiennent.
    Une caractéristique présente partout pèse peu ; une rare pèse beaucoup."""
    raise NotImplementedError


def vectoriser(carac: list[str], poids_idf: dict[str, float]) -> dict[str, float]:
    """Vecteur TF-IDF NORMALISÉ (norme euclidienne 1). tf = nombre d'occurrences.
    Une caractéristique inconnue de poids_idf est ignorée. Un vecteur vide reste vide."""
    raise NotImplementedError


def cosinus(u: dict[str, float], v: dict[str, float]) -> float:
    """Similarité cosinus de deux vecteurs creux (pas forcément normalisés).
    Piège de performance : parcourir le PLUS PETIT des deux dicts. Vecteur vide → 0.0."""
    raise NotImplementedError

"""LAB J3 — Dédoublonner un fichier clients « à peu près pareils ».

« Jean-Pierre DUPONT », « jean pierre Dupont » et « Jean-Piere Dupont » : même personne ?
Une égalité stricte (ou une jointure SQL) ne le voit pas. On va MESURER la ressemblance.

Étapes :
  1. normaliser     — rendre comparable (casse, accents, ponctuation, espaces)
  2. levenshtein    — distance d'édition, par programmation dynamique
  3. similarite     — ramener la distance entre 0 et 1
  4. cle_bloc       — ne comparer que les clients qui ont une chance d'être des doublons
  5. doublons_probables — assembler le tout

    uv run pytest j3/dedup
    uv run python -m j3.dedup.evaluer      ← précision, rappel, temps
"""
import unicodedata   # noqa: F401


def normaliser(texte: str) -> str:
    """'  Jean-Pierre  DUPONT ' → 'jean pierre dupont'.

    Minuscules, sans accents, tirets et apostrophes remplacés par des espaces,
    un seul espace entre les mots, pas d'espace au début ni à la fin.
    Indice : unicodedata.normalize("NFD", …) sépare la lettre de son accent ;
    l'accent a la catégorie Unicode "Mn".
    """
    raise NotImplementedError


def levenshtein(a: str, b: str) -> int:
    """Nombre minimal d'insertions, suppressions et remplacements pour passer de a à b.

    Programmation dynamique : un tableau (len(a)+1) × (len(b)+1) où la case [i][k] est
    la distance entre a[:i] et b[:k]. Objectif O(len(a) × len(b)).
    Bonus mémoire : ne garder que deux lignes du tableau.
    """
    raise NotImplementedError


def similarite(a: str, b: str) -> float:
    """1 - distance / longueur de la plus longue chaîne. Deux chaînes vides : 1.0."""
    raise NotImplementedError


def cle_bloc(client: dict) -> str:
    """Clé de « blocage » : seuls les clients de même clé seront comparés entre eux.

    Proposition de départ : code postal + première lettre du nom normalisé.
    À vous de mesurer ce qu'elle coûte en rappel (doublons manqués).
    """
    raise NotImplementedError


def doublons_probables(clients: list[dict], seuil: float = 0.85) -> set[tuple[str, str]]:
    """Paires d'ids (triées : (plus petit, plus grand)) dont « prénom nom » normalisés
    ont une similarité >= seuil, en ne comparant que les clients d'un même bloc.

    Comparer toutes les paires coûte n²/2 appels à levenshtein : 9 millions pour 4 500 clients.
    Avec des blocs, on n'en fait qu'une petite fraction.
    """
    raise NotImplementedError


# ------------------------------------------------------------ fourni
def evaluer(trouves: set, verite: set) -> dict:
    """Précision : parmi les paires trouvées, combien sont de vrais doublons ?
    Rappel : parmi les vrais doublons, combien ont été trouvés ?"""
    vrais_positifs = len(trouves & verite)
    return {
        "trouvees": len(trouves),
        "precision": vrais_positifs / len(trouves) if trouves else 1.0,
        "rappel": vrais_positifs / len(verite) if verite else 1.0,
    }

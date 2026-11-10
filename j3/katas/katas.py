"""EXERCICE 1 — Katas récursifs, en trois paliers.

Socle    : tout le monde doit les réussir.
Standard : l'objectif de l'heure.
Bonus    : pour ceux qui ont fini.

Pour chaque fonction récursive, écrivez D'ABORD le cas de base, ENSUITE le cas récursif.
Posez-vous la question : « mon appel récursif travaille-t-il sur un problème plus PETIT ? »

    uv run pytest j3/katas
"""


# ============================================================ SOCLE
def somme_chiffres(n: int) -> int:
    """somme_chiffres(1234) == 10. n >= 0. Récursif, sans str()."""
    raise NotImplementedError


def aplatir(liste: list) -> list:
    """aplatir([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]."""
    raise NotImplementedError


def puissance_rapide(x: float, n: int) -> float:
    """x ** n en O(log n) multiplications, n >= 0, sans l'opérateur **.

    Indice : x^10 = (x^5)², et x^5 = x × x^4.
    """
    raise NotImplementedError


# ============================================================ STANDARD
def taille_dossier(arbre: dict) -> int:
    """Taille totale d'un dossier et de tous ses sous-dossiers.

    arbre = {"nom": "src", "taille": 10, "enfants": [ {...}, {...} ]}
    """
    raise NotImplementedError


def sous_ensemble_somme(nombres: list[int], cible: int) -> list[int] | None:
    """Un sous-ensemble de nombres (tous POSITIFS) dont la somme vaut cible, ou None.

    Backtracking : on prend le premier nombre ou on ne le prend pas, et on abandonne
    une branche dès que la somme dépasse la cible (élagage).
    """
    raise NotImplementedError


def permutations(elements: list) -> list[list]:
    """Toutes les permutations, dans n'importe quel ordre. Interdit : itertools."""
    raise NotImplementedError


# ============================================================ BONUS
def n_reines(n: int) -> int:
    """Nombre de façons de placer n reines sur un échiquier n × n sans qu'elles se menacent.

    n_reines(8) == 92. Backtracking ligne par ligne, avec des set pour les colonnes et diagonales.
    """
    raise NotImplementedError


def profondeur(obj) -> int:
    """Profondeur d'imbrication de listes : profondeur(5) == 0, profondeur([[1], 2]) == 2.

    Piège : doit fonctionner sur une imbrication de 100 000 niveaux, SANS récursion
    et SANS toucher à sys.setrecursionlimit. Indice : une pile explicite (liste de (objet, niveau)).
    """
    raise NotImplementedError

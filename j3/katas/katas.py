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
    if n == 0:
        return 0

    return n % 10 + somme_chiffres(n // 10)


def aplatir(liste: list) -> list:
    """aplatir([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]."""
    res = []

    for elem in liste:
        if isinstance(elem, list):
            res.extend(aplatir(elem))
        else:
            res.append(elem)
    return res


def puissance_rapide(x: float, n: int) -> float:
    """x ** n en O(log n) multiplications, n >= 0, sans l'opérateur **.

    Indice : x^10 = (x^5)², et x^5 = x × x^4.
    """
    if n == 0:
        return 1

    moitie = puissance_rapide(x, n // 2)

    return moitie * moitie * (1 if n % 2 == 0 else x)


# ============================================================ STANDARD
arbre = {"nom": "projet", "taille": 4, "enfants": [
        {"nom": "src", "taille": 10, "enfants": [{"nom": "main.py", "taille": 3, "enfants": []}]},
        {"nom": "README", "taille": 1},
]}
def taille_dossier(arbre: dict) -> int:
    """Taille totale d'un dossier et de tous ses sous-dossiers.

    arbre = {"nom": "src", "taille": 10, "enfants": [ {...}, {...} ]}
    """
    total = arbre["taille"]

    if "enfants" in arbre:
        for enfant in arbre["enfants"]:
            total += taille_dossier(enfant)

    return total


def sous_ensemble_somme(nombres: list[int], cible: int) -> list[int] | None:
    """Un sous-ensemble de nombres (tous POSITIFS) dont la somme vaut cible, ou None.

    Backtracking : on prend le premier nombre ou on ne le prend pas, et on abandonne
    une branche dès que la somme dépasse la cible (élagage).
    """

    if cible == 0:
        # print('CAS DE BASE', nombres, cible)
        return []

    if not nombres or cible < 0:
        return None

    nombre_actuel = nombres[0]
    nombres_restants = nombres[1:]

    nouvelle_cible = cible - nombre_actuel

    # print(nombre_actuel, nombres_restants, nouvelle_cible)

    solution_avec_nb_actuel = sous_ensemble_somme(nombres_restants, nouvelle_cible)

    # print('solution avec nb actuel remonté : ', solution_avec_nb_actuel)

    if solution_avec_nb_actuel is not None:
        # print('NOT NONE')
        solution_avec_nb_actuel.append(nombre_actuel)
        return solution_avec_nb_actuel  

    solution_sans_nb_actuel = sous_ensemble_somme(nombres_restants, cible)

    return solution_sans_nb_actuel

print(sous_ensemble_somme([6, 30, 17], 36))


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

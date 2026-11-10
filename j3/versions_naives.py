"""J3 — Versions de référence, lentes mais simples. NE PAS MODIFIER."""


def fib_naif(n: int) -> int:
    """Fibonacci récursif sans mémoire : O(2^n) appels."""
    return n if n < 2 else fib_naif(n - 1) + fib_naif(n - 2)


def levenshtein_recursif(a: str, b: str) -> int:
    """Distance d'édition par la définition récursive. Exponentiel : chaînes courtes seulement."""
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a[0] == b[0]:
        return levenshtein_recursif(a[1:], b[1:])
    return 1 + min(levenshtein_recursif(a[1:], b),       # supprimer
                   levenshtein_recursif(a, b[1:]),       # insérer
                   levenshtein_recursif(a[1:], b[1:]))   # remplacer


def sac_a_dos_force_brute(objets: list[tuple[int, int]], capacite: int) -> int:
    """Valeur maximale en essayant les 2^n combinaisons. objets = [(poids, valeur), ...]."""
    if not objets:
        return 0
    (poids, valeur), reste = objets[0], objets[1:]
    sans = sac_a_dos_force_brute(reste, capacite)
    if poids > capacite:
        return sans
    return max(sans, valeur + sac_a_dos_force_brute(reste, capacite - poids))

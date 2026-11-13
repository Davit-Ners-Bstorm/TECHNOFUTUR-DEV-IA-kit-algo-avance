"""LAB J1 — Le bon choix de structure de données.

Pour chaque fonction :
  1. lis la version lente dans versions_naives.py ;
  2. mesure-la avec outils/mesure.py pour confirmer sa complexité ;
  3. écris ici une version rapide, avec la structure indiquée ;
  4. lance les tests :  uv run pytest j1/lab

Les signatures et le comportement attendu sont IDENTIQUES à versions_naives.py.
Chaque fonction a un budget de temps sur une grande entrée (tests marqués « perf »).
"""
from collections import deque          # noqa: F401  (utile pour moyenne_glissante)
import bisect                          # noqa: F401  (utile pour compter_dans_tranche)
from functools import cache
import heapq                           # noqa: F401  (utile pour top_k)


def doublons(emails: list[str]) -> list[str]:
    """Objectif : O(n). Indice : un `set` répond à « déjà vu ? » en temps constant."""
    vus: set[str] = set()
    signales: set[str] = set()
    resultat = []
    for e in emails:
        if e in vus and e not in signales:
            signales.add(e)
            resultat.append(e)
        vus.add(e)
    return resultat


def paires_somme(nombres: list[int], cible: int) -> bool:
    """Objectif : O(n), un seul parcours. Indice : pour chaque x, que cherches-tu ?"""
    vus: set[int] = set()
    for x in nombres:
        if cible - x in vus:      # on cherche le complément déjà rencontré
            return True
        vus.add(x)
    return False


def top_k(ventes: list[tuple[str, int]], k: int) -> list[tuple[str, int]]:
    """Objectif : O(n + m log k) avec m produits distincts.

    Indices : un `dict` pour les totaux, puis `heapq.nsmallest` avec une clé bien choisie.
    """
    totaux: dict[str, int] = {}
    for produit, qte in ventes:
        totaux[produit] = totaux.get(produit, 0) + qte
    # nsmallest sur (-total, produit) = plus grand total d'abord, égalités par ordre alphabétique
    return heapq.nsmallest(k, totaux.items(), key=lambda pt: (-pt[1], pt[0]))


def moyenne_glissante(valeurs: list[float], fenetre: int) -> list[float]:
    """Objectif : O(n). Indice : une somme courante ; on ajoute l'entrant, on retire le sortant.

    Bonus : utilise une `deque` pour la fenêtre, comme si les valeurs arrivaient en flux.
    """
    if fenetre <= 0:
            raise ValueError("la fenêtre doit être positive")
    resultat = []
    courante: deque[float] = deque()
    somme = 0.0
    for v in valeurs:
        courante.append(v)
        somme += v
        if len(courante) > fenetre:
            somme -= courante.popleft()   # O(1) avec une deque, O(n) avec list.pop(0)
        if len(courante) == fenetre:
            resultat.append(somme / fenetre)
    return resultat


def compter_dans_tranche(prix_tries: list[float], bas: float, haut: float) -> int:
    """Objectif : O(log n). Indice : `bisect_left` et `bisect_right`."""
    if bas > haut:
        return 0
    return bisect.bisect_right(prix_tries, haut) - bisect.bisect_left(prix_tries, bas)


# ---------------------------------------------------------------------------
# BONUS — mémoïsation avec frozendict (Python 3.15)
# ---------------------------------------------------------------------------
APPELS = {"tarif_lent": 0}


def tarif_lent(options: dict) -> float:
    """Calcul « coûteux » (imagine un appel réseau ou un modèle). Ne pas modifier."""
    APPELS["tarif_lent"] += 1
    base = 100.0
    if options.get("premium"):
        base *= 1.5
    return round(base * (1 - options.get("remise", 0) / 100), 2)

@cache
def _tarif_en_cache(options: frozendict) -> float:
    return tarif_lent(dict(options))


def tarif(options: dict) -> float:
    """Même résultat que tarif_lent, mais chaque combinaison d'options n'est calculée qu'une fois.

    Piège : `functools.cache` exige des arguments HACHABLES, et un dict ne l'est pas.
    Indice : convertis `options` en `frozendict` avant de passer par la fonction en cache."""
    return _tarif_en_cache(frozendict(options))

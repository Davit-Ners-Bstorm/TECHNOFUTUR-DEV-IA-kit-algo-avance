"""J2 — Versions de référence (lentes ou dangereuses). NE PAS MODIFIER.

Elles servent d'oracle dans les tests et de point de départ dans les exercices.
"""
import re


# ------------------------------------------------------------------ tris
def tri_insertion(lst: list) -> list:
    """Tri par insertion : simple, stable, O(n²)."""
    res = list(lst)
    for i in range(1, len(res)):
        x, k = res[i], i - 1
        while k >= 0 and res[k] > x:
            res[k + 1] = res[k]
            k -= 1
        res[k + 1] = x
    return res


def recherche_lineaire(lst: list, x) -> int:
    """Indice de la première occurrence de x, ou -1. O(n)."""
    for i, v in enumerate(lst):
        if v == x:
            return i
    return -1


# ------------------------------------------------------------------ jointures
# client  = (id, nom, ville)
# commande = (id, client_id, montant)     client_id peut valoir None
# résultat = (commande_id, nom_client, montant)

def jointure_boucles(clients: list[tuple], commandes: list[tuple]) -> list[tuple]:
    """Nested loop join : pour chaque commande, on parcourt tous les clients. O(n × m)."""
    res = []
    for cmd_id, client_id, montant in commandes:
        for cid, nom, _ville in clients:
            if client_id is not None and client_id == cid:
                res.append((cmd_id, nom, montant))
    return res


# ------------------------------------------------------------------ sécurité
NOM_REGEX = re.compile(r"^([A-Za-zÀ-ÿ'-]+\s?)*$")


def nom_valide_regex(nom: str) -> bool:
    """Validation par expression régulière. VULNÉRABLE au ReDoS (ne pas utiliser)."""
    return bool(NOM_REGEX.match(nom)) and 0 < len(nom) <= 100 and nom.strip() == nom


def verifier_jeton_naif(recu: str, attendu: str) -> bool:
    """Comparaison avec == : s'arrête au premier caractère différent (fuite par le temps)."""
    return recu == attendu

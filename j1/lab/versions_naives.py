"""Versions « débutant » : correctes, mais lentes.

C'est le code qu'on écrit naturellement après un premier module d'algorithmique.
NE PAS MODIFIER ce fichier : il sert
  - de point de départ au profilage (exercice 1) ;
  - d'ORACLE pour les tests de propriétés (exercice 3) : la version lente
    est simple, donc fiable ; on vérifie que la version rapide donne le même résultat.
"""


def doublons(emails: list[str]) -> list[str]:
    """Adresses présentes plus d'une fois, dans l'ordre de leur 2e apparition, sans répétition."""
    resultat = []
    for i, e in enumerate(emails):
        if e in emails[:i] and e not in resultat:   # deux parcours de liste à chaque tour
            resultat.append(e)
    return resultat


def paires_somme(nombres: list[int], cible: int) -> bool:
    """Existe-t-il deux positions i < j telles que nombres[i] + nombres[j] == cible ?"""
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if nombres[i] + nombres[j] == cible:
                return True
    return False


def top_k(ventes: list[tuple[str, int]], k: int) -> list[tuple[str, int]]:
    """Les k produits les plus vendus (total des quantités), du plus grand au plus petit.

    En cas d'égalité, ordre alphabétique du code produit.
    """
    totaux = []                          # liste de [produit, total]
    for produit, qte in ventes:
        for ligne in totaux:             # recherche linéaire dans la liste
            if ligne[0] == produit:
                ligne[1] += qte
                break
        else:
            totaux.append([produit, qte])
    totaux.sort(key=lambda l: (-l[1], l[0]))
    return [(p, t) for p, t in totaux[:k]]


def moyenne_glissante(valeurs: list[float], fenetre: int) -> list[float]:
    """Moyenne de chaque fenêtre de `fenetre` valeurs consécutives."""
    if fenetre <= 0:
        raise ValueError("la fenêtre doit être positive")
    return [sum(valeurs[i:i + fenetre]) / fenetre
            for i in range(len(valeurs) - fenetre + 1)]   # re-somme toute la fenêtre à chaque pas


def compter_dans_tranche(prix_tries: list[float], bas: float, haut: float) -> int:
    """Nombre de prix p tels que bas <= p <= haut. La liste est déjà triée."""
    return sum(1 for p in prix_tries if bas <= p <= haut)   # ignore que la liste est triée

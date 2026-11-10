"""AUDIT IA n°4 — Résolution de dépendances et plus court chemin.

Demande faite à l'assistant IA :
  « Écris une fonction qui lit le manifeste d'un paquet (un dict Python dans un fichier texte)
    et renvoie la liste de toutes ses dépendances à installer, dans l'ordre. Et une fonction
    qui trouve le chemin le plus court entre deux services de notre réseau. »

Les exemples du bas fonctionnent. Auditez avec la grille du J1 (au moins 6 problèmes).
"""


def lire_manifeste(texte: str) -> dict:
    """Le manifeste ressemble à : {"nom": "appli", "depend_de": ["a", "b"]}"""
    return eval(texte)


def a_installer(paquet: str, registre: dict[str, str], deja=[]) -> list[str]:
    """Toutes les dépendances de paquet, chaque dépendance avant ceux qui en ont besoin."""
    manifeste = lire_manifeste(registre[paquet])
    for dep in manifeste["depend_de"]:
        if dep not in deja:
            a_installer(dep, registre, deja)
    deja.append(paquet)
    return deja


def plus_court_chemin(reseau: dict[str, list[str]], a: str, b: str, chemin=None) -> list[str] | None:
    """Explore tous les chemins et garde le plus court."""
    chemin = (chemin or []) + [a]
    if a == b:
        return chemin
    meilleur = None
    for v in reseau.get(a, []):
        if v not in chemin:
            c = plus_court_chemin(reseau, v, b, chemin)
            if c and (meilleur is None or len(c) < len(meilleur)):
                meilleur = c
    return meilleur


if __name__ == "__main__":
    REGISTRE = {
        "appli": '{"nom": "appli", "depend_de": ["web", "orm"]}',
        "web": '{"nom": "web", "depend_de": ["url"]}',
        "orm": '{"nom": "orm", "depend_de": ["url"]}',
        "url": '{"nom": "url", "depend_de": []}',
    }
    print(a_installer("appli", REGISTRE))
    print(plus_court_chemin({"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}, "a", "d"))

"""Graphes FICTIFS pour le J4 : dépendances de paquets, pipeline de données, carte de trajets."""
import random

# ------------------------------------------------------------ paquets (A dépend de B)
# Noms inventés : toute ressemblance avec des paquets réels est fortuite.
DEPENDANCES = {
    "appli-web":        ["cadre-web", "orm-lite", "journal", "jeton-jwt"],
    "cadre-web":        ["routeur", "gabarits", "serveur-http"],
    "serveur-http":     ["analyse-url", "tls-outil"],
    "routeur":          ["analyse-url"],
    "gabarits":         ["echappe-html"],
    "orm-lite":         ["pilote-sql", "journal"],
    "pilote-sql":       ["tls-outil"],
    "jeton-jwt":        ["crypto-base", "horloge"],
    "tls-outil":        ["crypto-base"],
    "journal":          ["horloge"],
    "analyse-url":      [],
    "echappe-html":     [],
    "crypto-base":      [],
    "horloge":          [],
    "outil-cli":        ["analyse-args", "journal"],
    "analyse-args":     [],
}


def graphe_aleatoire(n: int, degre: int = 4, graine: int = 1) -> dict[int, list[int]]:
    """Graphe non orienté aléatoire de n sommets, pour les tests de performance."""
    rng = random.Random(graine)
    g = {i: [] for i in range(n)}
    for i in range(n):
        for _ in range(degre // 2):
            j = rng.randrange(n)
            if j != i:
                g[i].append(j); g[j].append(i)
    return g


# ------------------------------------------------------------ pipeline de données (tâche: durée, dépendances)
PIPELINE = {
    "extraire_crm":       (12, []),
    "extraire_boutique":  (8, []),
    "extraire_logs":      (20, []),
    "nettoyer_clients":   (15, ["extraire_crm", "extraire_boutique"]),
    "dedoublonner":       (25, ["nettoyer_clients"]),
    "pseudonymiser":      (5, ["dedoublonner"]),
    "agreger_logs":       (18, ["extraire_logs"]),
    "joindre":            (10, ["pseudonymiser", "agreger_logs"]),
    "calculer_embeddings": (40, ["joindre"]),
    "indexer_vecteurs":   (15, ["calculer_embeddings"]),
    "rapport_qualite":    (6, ["joindre"]),
    "publier":            (3, ["indexer_vecteurs", "rapport_qualite"]),
}

# ------------------------------------------------------------ carte de trajets (minutes, fictives)
TRAJETS = [
    ("Bruxelles", "Louvain", 30), ("Bruxelles", "Namur", 60), ("Bruxelles", "Mons", 65),
    ("Bruxelles", "Gand", 55), ("Bruxelles", "Anvers", 50), ("Bruxelles", "Wavre", 30),
    ("Wavre", "Namur", 40), ("Wavre", "Louvain", 35), ("Namur", "Liège", 50),
    ("Namur", "Charleroi", 40), ("Charleroi", "Mons", 45), ("Louvain", "Liège", 65),
    ("Liège", "Hasselt", 45), ("Hasselt", "Louvain", 50), ("Anvers", "Gand", 55),
    ("Gand", "Bruges", 40), ("Namur", "Mettet", 30), ("Charleroi", "Mettet", 30),
    ("Mettet", "Dinant", 25), ("Namur", "Dinant", 35), ("Dinant", "Arlon", 110), ("Namur", "Arlon", 105),
]


def carte_ponderee() -> dict[str, list[tuple[str, int]]]:
    g: dict[str, list[tuple[str, int]]] = {}
    for a, b, t in TRAJETS:
        g.setdefault(a, []).append((b, t))
        g.setdefault(b, []).append((a, t))
    return g


def grille(largeur: int = 60, hauteur: int = 40, densite: float = 0.25, graine: int = 3) -> list[str]:
    """Labyrinthe : '#' = mur, '.' = libre. Départ en haut à gauche, arrivée en bas à droite."""
    rng = random.Random(graine)
    lignes = []
    for y in range(hauteur):
        ligne = "".join("#" if rng.random() < densite else "." for _ in range(largeur))
        lignes.append(ligne)
    lignes[0] = "." + lignes[0][1:]
    lignes[-1] = lignes[-1][:-1] + "."
    return lignes

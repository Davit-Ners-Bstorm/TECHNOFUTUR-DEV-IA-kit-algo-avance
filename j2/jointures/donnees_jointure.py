"""Tables fictives pour le lab jointures (aucune donnée réelle)."""
import random

VILLES = ["Bruxelles", "Liège", "Namur", "Charleroi", "Mons", "Gand", "Anvers", "Louvain"]


def clients(n: int, graine: int = 1) -> list[tuple[int, str, str]]:
    rng = random.Random(graine)
    return [(i, f"Client {i:06d}", rng.choice(VILLES)) for i in range(1, n + 1)]


def commandes(m: int, n_clients: int, graine: int = 2,
              taux_orphelines: float = 0.02, taux_sans_client: float = 0.01) -> list[tuple]:
    """m commandes. Quelques-unes pointent vers un client inexistant (orphelines)
    ou n'ont pas de client du tout (None), comme dans les vraies bases."""
    rng = random.Random(graine)
    res = []
    for i in range(1, m + 1):
        r = rng.random()
        if r < taux_sans_client:
            cid = None
        elif r < taux_sans_client + taux_orphelines:
            cid = n_clients + rng.randint(1, 1000)       # client supprimé
        else:
            cid = rng.randint(1, n_clients)
        res.append((i, cid, round(rng.uniform(5, 500), 2)))
    return res

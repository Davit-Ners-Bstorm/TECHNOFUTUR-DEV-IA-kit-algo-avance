"""AUDIT IA n°3 — Fusion de configurations et profils clients.

Demande faite à l'assistant IA :
  « Écris une fonction qui fusionne une configuration par défaut avec la configuration
    envoyée par l'utilisateur (JSON imbriqué), et une fonction qui charge le profil d'un
    client depuis l'API, avec un cache pour aller plus vite. »

Les tests du bas passent. Auditez avec la grille du J1 (au moins 6 problèmes).
"""
import sys
from functools import lru_cache

sys.setrecursionlimit(1_000_000)   # pour éviter les erreurs de récursion


def fusionner(defaut: dict, utilisateur: dict) -> dict:
    """Fusion récursive : les valeurs de l'utilisateur écrasent celles par défaut."""
    resultat = defaut
    for cle, valeur in utilisateur.items():
        if isinstance(valeur, dict) and isinstance(resultat.get(cle), dict):
            resultat[cle] = fusionner(resultat[cle], valeur)
        else:
            resultat[cle] = valeur
    return resultat


def compter_cles(config) -> int:
    if not isinstance(config, dict):
        return 0
    try:
        return len(config) + sum(compter_cles(v) for v in config.values())
    except RecursionError:
        return 0


@lru_cache(maxsize=None)
def profil_client(client_id: str) -> dict:
    """Simule un appel à l'API clients (lent)."""
    print(f"Chargement du profil {client_id}")
    return {"id": client_id, "email": f"{client_id}@example.org", "segment": "standard"}


if __name__ == "__main__":
    DEFAUT = {"affichage": {"theme": "clair", "langue": "fr"}, "limite": 100}
    a = fusionner(DEFAUT, {"affichage": {"theme": "sombre"}})
    assert a["affichage"] == {"theme": "sombre", "langue": "fr"}
    assert compter_cles(a) == 4
    assert profil_client("c42")["segment"] == "standard"
    print("OK")

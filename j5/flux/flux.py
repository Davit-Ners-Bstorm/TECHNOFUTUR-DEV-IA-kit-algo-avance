"""BONUS DU MINI-PROJET — Algorithmes de flux : répondre vite avec peu de mémoire.

Cas d'usage dans le moteur : l'ingestion reçoit des millions de documents ; on veut savoir
« ai-je déjà indexé ce document ? » sans garder tous les identifiants en mémoire (Bloom),
et tirer un échantillon équitable pour évaluer la qualité, sans connaître la taille du flux (réservoir).

    uv run pytest j5/flux
"""
import hashlib   # noqa: F401
import random    # noqa: F401


class FiltreBloom:
    """Un tableau de n_bits bits et n_hash fonctions de hachage.

    ajouter(x)  : mettre à 1 les n_hash positions de x.
    contient(x) : True si TOUTES ses positions sont à 1.
    Garantie : jamais de faux négatif. Prix : quelques faux positifs.
    Indice : positions = int(hashlib.sha256(f"{i}:{x}".encode()).hexdigest(), 16) % n_bits, pour i de 0 à n_hash-1.
    Stocker les bits dans un bytearray (8 bits par octet) pour économiser la mémoire.
    """

    def __init__(self, n_bits: int, n_hash: int):
        raise NotImplementedError

    def ajouter(self, x: str) -> None:
        raise NotImplementedError

    def contient(self, x: str) -> bool:
        raise NotImplementedError


def echantillon_reservoir(flux, k: int, graine: int = 0) -> list:
    """k éléments tirés uniformément dans un flux de taille inconnue, en un seul passage, mémoire O(k).

    Algorithme R : garder les k premiers ; pour le i-ème élément suivant (i compté à partir de 0),
    tirer j au hasard entre 0 et i inclus ; si j < k, il remplace l'élément j du réservoir.
    """
    raise NotImplementedError

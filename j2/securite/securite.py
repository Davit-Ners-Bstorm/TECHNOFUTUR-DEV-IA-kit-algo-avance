"""EXERCICE SÉCURITÉ — Quand la complexité devient une faille.

Trois fonctions à rendre sûres. Les versions dangereuses sont dans j2/versions_naives.py.

    uv run pytest j2/securite
    uv run python -m j2.securite.demo_redos     ← voir le ReDoS en direct
"""
import hmac            # noqa: F401
from urllib.parse import parse_qs   # noqa: F401

LONGUEUR_MAX_NOM = 100
MAX_PARAMETRES = 100


def nom_valide(nom: str) -> bool:
    """Même règle que nom_valide_regex, mais en temps LINÉAIRE garanti :
      - 1 à 100 caractères ;
      - uniquement lettres (accents compris), espaces, tirets et apostrophes ;
      - pas d'espace au début ni à la fin.
    Indice : str.isalpha() reconnaît les lettres accentuées. Vérifiez la LONGUEUR EN PREMIER.
    """
    raise NotImplementedError


def verifier_jeton(recu: str, attendu: str) -> bool:
    """Compare deux jetons en temps constant, sans fuite par le temps de réponse.

    Indice : hmac.compare_digest. Piège : il refuse les str non ASCII → comparez des bytes.
    """
    raise NotImplementedError


def lire_parametres(chaine_requete: str) -> dict[str, list[str]]:
    """Décode une chaîne de requête HTTP (« a=1&b=2 ») en dict.

    Défense contre le déni de service : au-delà de MAX_PARAMETRES champs, lever ValueError
    AVANT de remplir le dictionnaire. Indice : un paramètre de parse_qs fait exactement ça.
    """
    raise NotImplementedError

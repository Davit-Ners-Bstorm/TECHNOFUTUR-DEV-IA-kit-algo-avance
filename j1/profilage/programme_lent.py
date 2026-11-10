"""EXERCICE 1 — Trouver où le temps passe.

Ce programme prépare un rapport de fin de journée pour une boutique en ligne.
Il « marche », mais il est lent. Ta mission : trouver POURQUOI, sans deviner.

1. Lance-le et chronomètre-le :
       uv run python -m j1.profilage.programme_lent

2. Profile-le avec le profileur par échantillonnage de Python 3.15 :
       uv run python -m profiling.sampling run --flamegraph -o profil.html -m j1.profilage.programme_lent
   Ouvre profil.html dans ton navigateur : plus une barre est large, plus la fonction coûte.

3. Version tableau (compatible pstats) :
       uv run python -m profiling.sampling run -m j1.profilage.programme_lent

4. Pour la fonction la plus coûteuse, mesure sa croissance avec outils.mesure
   (voir mesurer_croissance.py) et complète la fiche fiche_mesures.md.
"""
import time

from j1.lab import versions_naives as naif
from outils import donnees


def rapport(n: int = 20_000) -> dict:
    emails = donnees.emails(n)
    ventes = donnees.ventes(n * 5)
    capteur = donnees.mesures_capteur(n * 5)
    prix = donnees.prix_tries(n)

    return {
        "clients_en_double": len(naif.doublons(emails)),
        "top_5": naif.top_k(ventes, 5),
        "temperature_lissee_max": max(naif.moyenne_glissante(capteur, 1_000)),
        "articles_10_50_eur": naif.compter_dans_tranche(prix, 10, 50),
        "promo_possible": naif.paires_somme([round(p) for p in prix[:3_000]], 2_001),
    }


if __name__ == "__main__":
    debut = time.perf_counter()
    resultat = rapport()
    for cle, valeur in resultat.items():
        print(f"{cle:>24} : {valeur}")
    print(f"\nDurée totale : {time.perf_counter() - debut:.2f} s")

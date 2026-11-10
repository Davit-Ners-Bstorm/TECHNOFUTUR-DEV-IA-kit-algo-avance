"""Mesurer la croissance d'une fonction en doublant la taille de l'entrée.

    uv run python -m j1.profilage.mesurer_croissance

Exemple fourni pour `doublons`. Ajoute les autres fonctions en suivant le même modèle.
"""
from j1.lab import versions_naives as naif
from outils import donnees
from outils.mesure import afficher_croissance, mesurer, pic_memoire

TAILLES = [1_000, 2_000, 4_000, 8_000]

print("doublons (version naïve)")
afficher_croissance(mesurer(naif.doublons, lambda n: (donnees.emails(n),), TAILLES))

print("\nPic mémoire pour 8 000 e-mails :",
      pic_memoire(naif.doublons, donnees.emails(8_000)) // 1024, "Kio")

# À TOI : top_k, moyenne_glissante (fenêtre 500), compter_dans_tranche, paires_somme.
# Attention : pour paires_somme, choisis une cible impossible, sinon tu mesures la chance.

"""Dijkstra contre A* sur un labyrinthe : même chemin, combien de cases explorées ?

    uv run python -m j4.chemins.comparer
"""
import time

from j4.donnees_graphes import grille
from outils.choix import charger

ch = charger("j4.chemins.chemins")

for largeur, hauteur in [(60, 40), (200, 120), (600, 400)]:
    g = grille(largeur, hauteur)
    arrivee = (hauteur - 1, largeur - 1)
    print(f"\nLabyrinthe {largeur} × {hauteur} ({largeur * hauteur} cases)")
    for nom, h in [("Dijkstra (sans heuristique)", False), ("A* (Manhattan)", True)]:
        debut = time.perf_counter()
        res = ch.a_etoile(g, (0, 0), arrivee, heuristique=h)
        duree = time.perf_counter() - debut
        if res is None:
            print(f"  {nom:<28} pas de chemin")
        else:
            print(f"  {nom:<28} longueur {res[0]:>4}   cases explorées {res[1]:>7}   {duree:.3f} s")

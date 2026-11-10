"""Mesurer la qualité et le coût de la déduplication.

    uv run python -m j3.dedup.evaluer

Pour la fiche : faites varier le seuil (0.75, 0.85, 0.95) et la clé de bloc.
Que gagne-t-on en temps ? Que perd-on en rappel ? Pourquoi la précision n'atteint-elle jamais 100 % ?
"""
import time

from j3.dedup.donnees_clients import generer
from outils.choix import charger

dd = charger("j3.dedup.dedup")
clients, verite = generer()
print(f"{len(clients)} clients, {len(verite)} vraies paires de doublons")
n = len(clients)
print(f"Sans blocs : {n * (n - 1) // 2:,} comparaisons".replace(",", " "))

blocs = {}
for c in clients:
    blocs.setdefault(dd.cle_bloc(c), 0)
    blocs[dd.cle_bloc(c)] += 1
comparaisons = sum(t * (t - 1) // 2 for t in blocs.values())
print(f"Avec blocs : {comparaisons:,} comparaisons ({len(blocs)} blocs)".replace(",", " "))

print(f"\n{'seuil':>6} | {'trouvées':>8} | {'précision':>9} | {'rappel':>6} | temps")
for seuil in (0.75, 0.85, 0.95):
    debut = time.perf_counter()
    trouves = dd.doublons_probables(clients, seuil)
    duree = time.perf_counter() - debut
    m = dd.evaluer(trouves, verite)
    print(f"{seuil:>6} | {m['trouvees']:>8} | {m['precision']:>9.1%} | {m['rappel']:>6.1%} | {duree:.2f} s")

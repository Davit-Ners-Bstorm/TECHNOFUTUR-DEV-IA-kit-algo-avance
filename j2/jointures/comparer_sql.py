"""Comparer vos jointures à deux moteurs SQL : SQLite (inclus dans Python) et DuckDB.

    uv run python -m j2.jointures.comparer_sql

Le script :
  1. charge les mêmes tables dans SQLite et DuckDB (requêtes PARAMÉTRÉES, jamais de f-string) ;
  2. affiche le PLAN D'EXÉCUTION choisi par chaque moteur ;
  3. chronomètre chaque moteur et chacune de vos jointures.

Pour la fiche : quel algorithme chaque moteur a-t-il choisi ? Que change l'ajout d'une
clé primaire dans SQLite ? Où se situent vos versions Python ?
"""
import sqlite3
import time

import duckdb

from j2 import versions_naives as naif
from j2.jointures import donnees_jointure as dj
from outils.choix import charger

j = charger("j2.jointures.jointures")
N_CLIENTS, N_COMMANDES = 50_000, 300_000
REQUETE = ("SELECT cmd.id, cli.nom, cmd.montant FROM commandes cmd "
           "JOIN clients cli ON cmd.client_id = cli.id")


def chrono(nom, f):
    debut = time.perf_counter()
    res = f()
    print(f"  {nom:<38} {time.perf_counter() - debut:7.3f} s   {len(res):>8} lignes")
    return res


cli, cmd = dj.clients(N_CLIENTS), dj.commandes(N_COMMANDES, N_CLIENTS)

# ---------------------------------------------------------------- SQLite
s = sqlite3.connect(":memory:")
s.execute("CREATE TABLE clients(id INTEGER, nom TEXT, ville TEXT)")
s.execute("CREATE TABLE clients_pk(id INTEGER PRIMARY KEY, nom TEXT, ville TEXT)")
s.execute("CREATE TABLE commandes(id INTEGER, client_id INTEGER, montant REAL)")
s.executemany("INSERT INTO clients VALUES (?, ?, ?)", cli)
s.executemany("INSERT INTO clients_pk VALUES (?, ?, ?)", cli)
s.executemany("INSERT INTO commandes VALUES (?, ?, ?)", cmd)

print("\n=== Plans d'exécution ===")
print("SQLite, sans clé primaire :")
for ligne in s.execute("EXPLAIN QUERY PLAN " + REQUETE):
    print("   ", ligne[-1])
print("SQLite, avec clé primaire :")
for ligne in s.execute("EXPLAIN QUERY PLAN " + REQUETE.replace("clients cli", "clients_pk cli")):
    print("   ", ligne[-1])

d = duckdb.connect()
d.execute("CREATE TABLE clients(id INTEGER, nom VARCHAR, ville VARCHAR)")
d.execute("CREATE TABLE commandes(id INTEGER, client_id INTEGER, montant DOUBLE)")
d.executemany("INSERT INTO clients VALUES (?, ?, ?)", cli)
d.executemany("INSERT INTO commandes VALUES (?, ?, ?)", cmd)
print("DuckDB :")
print(d.execute("EXPLAIN " + REQUETE).fetchall()[0][1])

print(f"\n=== Chronomètre ({N_CLIENTS} clients × {N_COMMANDES} commandes) ===")
chrono("SQLite sans clé primaire", lambda: s.execute(REQUETE).fetchall())
chrono("SQLite avec clé primaire",
       lambda: s.execute(REQUETE.replace("clients cli", "clients_pk cli")).fetchall())
chrono("DuckDB", lambda: d.execute(REQUETE).fetchall())
for nom in ["jointure_hachage", "jointure_tri_fusion"]:
    try:
        chrono(f"Python — {nom}", lambda: getattr(j, nom)(cli, cmd))
    except NotImplementedError:
        print(f"  Python — {nom:<29} (pas encore écrite)")
petit_cli, petit_cmd = cli[:2_000], cmd[:20_000]
chrono("Python — boucles (2 000 × 20 000 seulement !)", lambda: naif.jointure_boucles(petit_cli, petit_cmd))

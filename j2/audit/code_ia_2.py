"""AUDIT IA n°2 — Rapport des meilleurs clients d'une ville.

Demande faite à l'assistant IA :
  « Écris une fonction qui, pour une ville donnée, renvoie les 5 clients qui ont dépensé
    le plus, à partir d'une base SQLite. Protège la fonction par une clé d'API. »

Le code fonctionne sur l'exemple du bas. Auditez-le avec j1/audit/grille_audit.md.
Indice : il y a au moins 6 problèmes, dont 2 de sécurité graves.
"""
import sqlite3

CLE_API = "cle-secrete-2026"


def meilleurs_clients(con, ville, cle_api):
    if cle_api != CLE_API:
        return []
    try:
        clients = con.execute(f"SELECT id, nom FROM clients WHERE ville = '{ville}'").fetchall()
        commandes = con.execute("SELECT client_id, montant FROM commandes").fetchall()
        totaux = []
        for cid, nom in clients:
            total = 0
            for client_id, montant in commandes:
                if client_id == cid:
                    total += montant
            totaux.append((nom, total))
            totaux = sorted(totaux, key=lambda t: t[1], reverse=True)
        return totaux[:5]
    except Exception:
        return []


if __name__ == "__main__":
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE clients(id INTEGER, nom TEXT, ville TEXT)")
    con.execute("CREATE TABLE commandes(id INTEGER, client_id INTEGER, montant REAL)")
    con.executemany("INSERT INTO clients VALUES (?, ?, ?)",
                    [(1, "Alice", "Namur"), (2, "Bruno", "Namur"), (3, "Chloé", "Mons")])
    con.executemany("INSERT INTO commandes VALUES (?, ?, ?)",
                    [(1, 1, 50.0), (2, 2, 80.0), (3, 1, 40.0), (4, 3, 500.0)])
    print(meilleurs_clients(con, "Namur", "cle-secrete-2026"))

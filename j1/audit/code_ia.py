"""EXERCICE 4 — Audit d'un code généré par IA.

Contexte : un collègue a demandé à un assistant IA :
  « Écris une fonction Python qui fusionne deux listes de clients (CRM et boutique),
    supprime les doublons par e-mail, valide les noms, et calcule le taux de doublons. »

L'assistant a produit le code ci-dessous. Il passe le test du collègue (en bas du fichier).
Ta mission : l'auditer avec la grille grille_audit.md AVANT qu'il parte en production.
Ne le corrige pas tout de suite : d'abord trouver, classer, justifier.
"""
import re

NOM_VALIDE = re.compile(r"^([A-Za-zÀ-ÿ]+\s?)*$")


def nettoyer(email):
    return email.strip()


def fusionner_clients(crm, boutique, rejetes=[]):
    """Fusionne deux listes de clients {'nom': ..., 'email': ...} sans doublons."""
    resultat = []
    emails_vus = []
    for client in crm + boutique:
        email = nettoyer(client["email"])
        if not NOM_VALIDE.match(client["nom"]):
            print(f"Client rejeté : {client['nom']} <{email}>")
            rejetes.append(client)
            continue
        if email not in emails_vus:
            emails_vus.append(email)
            resultat.append(client)
    taux = (len(crm) + len(boutique) - len(resultat)) / (len(crm) + len(boutique))
    return sorted(resultat, key=lambda c: c["nom"]), taux


if __name__ == "__main__":
    crm = [{"nom": "Alice Dupont", "email": "alice@example.org"}]
    boutique = [{"nom": "Alice Dupont", "email": "alice@example.org "},
                {"nom": "Bruno Maes", "email": "bruno@example.org"}]
    clients, taux = fusionner_clients(crm, boutique)
    assert len(clients) == 2
    print("OK", clients, f"taux de doublons : {taux:.0%}")

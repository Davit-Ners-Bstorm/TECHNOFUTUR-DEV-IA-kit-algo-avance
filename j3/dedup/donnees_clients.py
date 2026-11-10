"""Fichier clients FICTIF avec des doublons « à peu près pareils », et la vérité terrain.

Aucune donnée réelle. Les identifiants sont pseudonymisés : un HMAC du numéro interne avec
une clé secrète. Sans la clé, on ne remonte pas au numéro interne ; avec elle, on peut
toujours rapprocher les enregistrements. C'est de la pseudonymisation, PAS de l'anonymisation :
au sens du RGPD, ce sont toujours des données personnelles.
"""
import hashlib
import hmac
import random

PRENOMS = ["Jean-Pierre", "Marie", "Élodie", "François", "Anne-Sophie", "Luc", "Hélène", "Mathéo",
           "Chloé", "Noël", "Inès", "Benoît", "Céline", "Jérôme", "Zoé", "Raphaël", "Léa", "Hugo",
           "Amélie", "Thibaut", "Sébastien", "Ophélie", "Karim", "Fatima", "Pieter", "Annelies",
           "Wouter", "Sofie", "Yasmine", "Mehdi", "Bérénice", "Gaëtan", "Joëlle", "Loïc",
           "Adrien", "Bastien", "Camille", "Damien", "Estelle", "Florian", "Gwendoline", "Henri",
           "Isabelle", "Julien", "Kevin", "Laurence", "Maxime", "Nathalie", "Olivier", "Pascale",
           "Quentin", "Romain", "Sarah", "Thomas", "Valérie", "William", "Xavier", "Yannick",
           "Aurélie", "Bruno", "Cédric", "Delphine", "Emma", "Frédéric", "Géraldine", "Ilias"]
NOMS = ["Dupont", "Van den Broeck", "Peeters", "Janssens", "Lambert", "Dubois", "Willems", "Claes",
        "Goossens", "Mertens", "De Smet", "Lemaire", "Hermans", "Renard", "Leroy", "Desmet",
        "Van Damme", "Wouters", "Maes", "Jacobs", "Mahieu", "Collignon", "D'Hondt", "Delvaux",
        "El Amrani", "Benali", "Nguyen", "Kowalski", "Fontaine", "Vandenberghe", "Dumont", "Gilson",
        "Bastin", "Charlier", "Denis", "Evrard", "François", "Gérard", "Henrard", "Jacquet",
        "Lejeune", "Martin", "Noël", "Piron", "Remy", "Simon", "Thiry", "Urbain", "Verhaegen",
        "Wilmotte", "Ysebaert", "Zimmer", "Bodart", "Closset", "Dethier", "Englebert", "Fraikin",
        "Gillet", "Hubert", "Istasse", "Jadot", "Kaisin", "Lecomte", "Mathy", "Nicolay"]
CODES_POSTAUX = ["1000", "1050", "1060", "1070", "1180", "1200", "1300", "1348", "1400", "1420",
                 "4000", "4020", "4800", "5000", "5030", "5100", "5500", "5640", "6000", "6200",
                 "6700", "7000", "7100", "7500", "8000", "8500", "9000", "9300", "2000", "3000"]
CLE_PSEUDO = b"cle-de-formation-ne-pas-reutiliser"


def pseudo_id(numero_interne: int) -> str:
    return hmac.new(CLE_PSEUDO, str(numero_interne).encode(), hashlib.sha256).hexdigest()[:12]


def _faute_de_frappe(s: str, rng: random.Random) -> str:
    if len(s) < 4:
        return s
    i = rng.randrange(1, len(s) - 1)
    choix = rng.random()
    if choix < 0.33:                                  # inversion de deux lettres
        return s[:i] + s[i + 1] + s[i] + s[i + 2:]
    if choix < 0.66:                                  # lettre oubliée
        return s[:i] + s[i + 1:]
    return s[:i] + rng.choice("aeinrst") + s[i:]      # lettre en trop


def _variante(prenom: str, nom: str, rng: random.Random) -> tuple[str, str]:
    import unicodedata
    for _ in range(rng.randint(1, 2)):
        t = rng.random()
        if t < 0.25:
            prenom, nom = prenom.upper(), nom.upper()
        elif t < 0.5:
            sans = lambda s: "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
            prenom, nom = sans(prenom), sans(nom)
        elif t < 0.7:
            prenom = prenom.replace("-", " ")
        elif t < 0.85:
            nom = _faute_de_frappe(nom, rng)
        else:
            prenom = _faute_de_frappe(prenom, rng)
    return prenom, "  " + nom if rng.random() < 0.1 else nom


def generer(n: int = 4_000, taux_doublons: float = 0.12, taux_demenagement: float = 0.1,
            graine: int = 7) -> tuple[list[dict], set[tuple[str, str]]]:
    """Renvoie (clients, vrais_doublons). Un doublon sur dix a changé de code postal (déménagement)."""
    rng = random.Random(graine)
    clients, verite, numero = [], set(), 0
    for _ in range(n):
        numero += 1
        c = {"id": pseudo_id(numero), "prenom": rng.choice(PRENOMS), "nom": rng.choice(NOMS),
             "code_postal": rng.choice(CODES_POSTAUX)}
        clients.append(c)
    originaux = list(clients)
    groupes = {c["id"]: [c["id"]] for c in originaux}
    for _ in range(int(n * taux_doublons)):
        o = rng.choice(originaux)
        numero += 1
        prenom, nom = _variante(o["prenom"], o["nom"], rng)
        cp = rng.choice(CODES_POSTAUX) if rng.random() < taux_demenagement else o["code_postal"]
        d = {"id": pseudo_id(numero), "prenom": prenom, "nom": nom, "code_postal": cp}
        clients.append(d)
        groupes[o["id"]].append(d["id"])
    for ids in groupes.values():              # deux variantes du même client sont aussi des doublons
        for i in range(len(ids)):
            for k in range(i + 1, len(ids)):
                verite.add(tuple(sorted((ids[i], ids[k]))))
    rng.shuffle(clients)
    # Homonymes : même nom ET même code postal, mais personnes différentes → pièges volontaires.
    return clients, verite

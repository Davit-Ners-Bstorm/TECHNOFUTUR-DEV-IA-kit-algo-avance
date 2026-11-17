"""LAB J2 — Comment une base de données fait une jointure.

Équivalent SQL de ce que vous allez écrire :

    SELECT cmd.id, cli.nom, cmd.montant
    FROM commandes cmd JOIN clients cli ON cmd.client_id = cli.id

Formats :
    client   = (id, nom, ville)
    commande = (id, client_id, montant)     ← client_id peut être None
    résultat = liste de (commande_id, nom_client, montant), dans n'importe quel ordre

Règles SQL à respecter (les tests les vérifient) :
    - une commande sans client correspondant n'apparaît pas (jointure INTERNE) ;
    - None ne correspond à rien, pas même à None ;
    - si un id client apparaît deux fois (données sales !), la commande sort deux fois.

La version « boucles imbriquées » est dans j2/versions_naives.py : c'est votre oracle.

    uv run pytest j2/jointures
    uv run python -m j2.jointures.comparer_sql
"""

# clients = [(1, "Alice", "Namur"), (2, "Bruno", "Mons")]
# commandes = [(10, 2, 50.0), (11, 1, 20.0), (12, 3, 9.0), (13, None, 1.0)]

def jointure_hachage(clients: list[tuple], commandes: list[tuple]) -> list[tuple]:
    """Hash join. Objectif O(n + m).

    Phase 1 (build) : un dict id → liste des noms, construit sur la PLUS PETITE table.
    Phase 2 (probe) : on parcourt l'autre table et on cherche chaque clé dans le dict.
    """

    client_index = dict()

    for id, nom, ville in clients:
        if id is None:
            continue

        if id not in client_index:
            client_index[id] = []

        client_index[id].append(nom)

    resultat = []

    for commande_id, client_id, prix in commandes:
        if client_id in client_index:
            for nom in client_index[client_id]:
                resultat.append((nom, client_id, commande_id, prix))

    return resultat

# print(jointure_hachage([(1, "Alice", "Namur"), (2, "Bruno", "Mons")], [(10, 2, 50.0), (11, 1, 20.0), (12, 3, 9.0), (13, None, 1.0)]))




def jointure_tri_fusion(clients: list[tuple], commandes: list[tuple]) -> list[tuple]:
    """Sort-merge join. Objectif O(n log n + m log m).

    1. Trier les deux tables sur la clé de jointure (sorted avec key= est autorisé ici).
    2. Avancer deux curseurs en parallèle, comme dans la fusion du tri fusion.
    Piège : quand la même clé apparaît plusieurs fois des deux côtés, il faut produire
    TOUTES les combinaisons. Pensez « groupe de clés égales ».
    """

    clients_sorted = sorted((c for c in clients if c[0] is not None), key= lambda c: c[0])
    commandes_sorted = sorted((c for c in commandes if c[1] is not None), key= lambda c: c[1])

    i = 0
    j = 0

    resultat = []

    while i < len(clients_sorted) and j < len(commandes_sorted):
        client_id = clients_sorted[i][0]
        commande_client_id = commandes_sorted[j][1]

        if client_id < commande_client_id:
            i += 1

        elif client_id > commande_client_id:
            j += 1

        else:
            groupe_client = []

            while i < len(clients_sorted) and clients_sorted[i][0] == client_id:
                groupe_client.append(clients_sorted[i])
                i += 1

            groupe_commandes = []

            while j < len(commandes_sorted) and commandes_sorted[j][1] == client_id:
                groupe_commandes.append(commandes_sorted[j])
                j += 1

            for cl in groupe_client:
                for co in groupe_commandes:
                    resultat.append(
                        (cl[1],
                        co[0],
                        co[2])
                    )
    return resultat

# print(jointure_tri_fusion([(1, "Alice", "Namur"), (None, "Alice", "Namur"), (2, "Bruno", "Mons"), (2, "Test", "Mons")], [(1, 2, 50.0), (18, 2, 26), (11, 1, 20.0), (12, 3, 9.0), (13, None, 1.0)]))
    


def jointure_gauche(clients: list[tuple], commandes: list[tuple]) -> list[tuple]:
    """BONUS — LEFT JOIN : toutes les commandes, avec nom_client = None si pas de client.

    Équivalent : SELECT ... FROM commandes cmd LEFT JOIN clients cli ON ...
    """
    raise NotImplementedError

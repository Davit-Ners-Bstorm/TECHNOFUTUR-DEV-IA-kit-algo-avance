clients = [
    { "id": 1, "nom": 'Bob'},
    { "id": 2, "nom": 'Alice'},
    { "id": 3, "nom": 'Grégoire'},
]

commandes = [
    { "id": 1, "client_id": 2 },
    { "id": 2, "client_id": 1 },
    { "id": 3, "client_id": 3 },
]

def search_naif(clients_lst, commandes_lst):
    resultats = []

    for c in commandes_lst:
        for cl in clients_lst:
            if c["client_id"] == cl["id"]:
                print(c, cl)

search_naif(clients, commandes)


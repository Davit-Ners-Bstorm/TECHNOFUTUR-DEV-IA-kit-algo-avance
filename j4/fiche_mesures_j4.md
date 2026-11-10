# Fiche de mesures — J4

## 1. Parcours

Faille dans `crypto-base` : quels paquets sont impactés ? ……

Combien de « sauts » entre `appli-web` et `crypto-base` au plus court ? Quel chemin ? ……

## 2. Ordonnanceur (`uv run python -m j4.ordonnanceur.planifier`)

| Mesure | Valeur |
|---|---|
| Nombre de vagues parallèles | |
| Durée minimale du pipeline | |
| Somme de toutes les durées (une seule machine) | |
| Tâches du chemin critique | |

Si `calculer_embeddings` passe de 40 à 20 min, la durée totale baisse-t-elle de 20 min ? Pourquoi ? ……

Si `agreger_logs` passe de 18 à 5 min, que se passe-t-il ? Pourquoi ? ……

## 3. Dijkstra et A* (`uv run python -m j4.chemins.comparer`)

| Labyrinthe | Cases explorées Dijkstra | Cases explorées A* | Rapport |
|---|---|---|---|
| 60 × 40 | | | |
| 200 × 120 | | | |
| 600 × 400 | | | |

Pourquoi A* trouve-t-il un chemin de la même longueur en explorant moins ? ……

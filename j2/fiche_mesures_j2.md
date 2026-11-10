# Fiche de mesures — J2

## 1. Tris (`uv run python -m j2.tris.chronometrer`)

| Tri | Ratio quand n double | Complexité mesurée | Temps pour 16 000 éléments |
|---|---|---|---|
| tri_insertion (naïf) | | | |
| tri_fusion | | | |
| tri_rapide | | | |
| sorted() | | | |

Pourquoi `sorted()` est-il bien plus rapide que `tri_fusion`, alors qu'ils ont la même complexité ? ……

Que devient `sorted()` sur une liste déjà triée ? Pourquoi ? ……

## 2. Jointures (`uv run python -m j2.jointures.comparer_sql`)

| Moteur ou fonction | Algorithme utilisé (d'après le plan) | Temps |
|---|---|---|
| SQLite sans clé primaire | | |
| SQLite avec clé primaire | | |
| DuckDB | | |
| Python — jointure_hachage | hash join | |
| Python — jointure_tri_fusion | sort-merge join | |
| Python — boucles (petites tables) | nested loop | |

Qu'est-ce qui change dans le plan SQLite quand on ajoute une clé primaire ? ……

Dans quel cas un moteur préfère-t-il un sort-merge join à un hash join ? ……

# Développeur IA 2026 — Algorithmes avancés

Exercices et labs du module (5 jours), un dossier `jN` par journée.

## Installation (une seule fois)

1. Installe **uv** (version récente : les anciennes versions ne connaissent pas Python 3.15).
2. Dans ce dossier :

```bash
uv sync          # installe Python 3.15, pytest, Hypothesis dans .venv
uv run pytest    # lance les tests : au début, presque tout échoue, c'est normal
```

## Journée 1 — Mesurer avant d'optimiser

| Exercice | Dossier | Commande |
|---|---|---|
| 1. Profiler un programme lent | `j1/profilage` | `uv run python -m j1.profilage.programme_lent` |
| 2. Lab : la bonne structure de données | `j1/lab` | `uv run pytest j1/lab` |
| 3. Tests par propriétés | `j1/proprietes` | `uv run pytest j1/proprietes` |
| 4. Audit d'un code généré par IA | `j1/audit` | lire `code_ia.py`, remplir `grille_audit.md` |

## Journée 2 — Recherche, tri et jointures

| Exercice | Dossier | Commande |
|---|---|---|
| 1. Recherche et tris (guidé) | `j2/tris` | `uv run pytest j2/tris` puis `uv run python -m j2.tris.chronometrer` |
| 2. Lab : les trois jointures | `j2/jointures` | `uv run pytest j2/jointures` puis `uv run python -m j2.jointures.comparer_sql` |
| 3. Sécurité algorithmique | `j2/securite` | `uv run python -m j2.securite.demo_redos` puis `uv run pytest j2/securite` |
| 4. Audit IA n°2 | `j2/audit` | lire `code_ia_2.py`, remplir la grille du J1 |

Fiche à compléter : `j2/fiche_mesures_j2.md`.

## Journée 3 — Récursion et programmation dynamique

| Exercice | Dossier | Commande |
|---|---|---|
| Démos (formateur) | `j3/demos` | `uv run python -m j3.demos.fibonacci`, `… j3.demos.sac_a_dos` |
| 1. Katas récursifs à paliers | `j3/katas` | `uv run pytest j3/katas` |
| 2. Lab : déduplication fuzzy | `j3/dedup` | `uv run pytest j3/dedup` puis `uv run python -m j3.dedup.evaluer` |
| 3. Audit IA n°3 | `j3/audit` | lire `code_ia_3.py`, remplir la grille du J1 |

Fiche à compléter : `j3/fiche_mesures_j3.md`.

## Journée 4 — Graphes

| Exercice | Dossier | Commande |
|---|---|---|
| 1. Parcours d'un réseau de dépendances | `j4/parcours` | `uv run pytest j4/parcours` |
| 2. Lab : ordonnanceur de pipeline | `j4/ordonnanceur` | `uv run pytest j4/ordonnanceur` puis `uv run python -m j4.ordonnanceur.planifier` |
| 2 bis. Lab : plus courts chemins | `j4/chemins` | `uv run pytest j4/chemins` puis `uv run python -m j4.chemins.comparer` |
| 3. Audit IA n°4 | `j4/audit` | lire `code_ia_4.py`, remplir la grille du J1 |

Fiche à compléter : `j4/fiche_mesures_j4.md`.

## Journée 5 — Les algorithmes au cœur d'un RAG

| Exercice | Dossier | Commande |
|---|---|---|
| 1. Tokenisation BPE à la main | `j5/bpe` | `uv run pytest j5/bpe` |
| 2. Mini-projet : moteur de recherche | `j5/moteur` | `uv run pytest j5/moteur`, puis `uv run python -m j5.moteur.evaluer` et `… passage_echelle` |
| Bonus : algorithmes de flux | `j5/flux` | `uv run pytest j5/flux` |
| Démos (formateur) | `j5/demos` | `uv run python -m j5.demos.flux_demo`, `… j5.demos.vers_numpy` |

Fiche : `j5/fiche_mesures_j5.md`. Auto-évaluation : `j5/grille_mini_projet.md`.

Outils communs : `outils/mesure.py` (chronométrer, mesurer la croissance et la mémoire)
et `outils/donnees.py` (jeux de données **fictifs** et reproductibles).

## Règles du jeu

- Ne modifie pas `versions_naives.py` : c'est la référence (l'« oracle »).
- Un test vert ne suffit pas : mesure le gain et note-le dans `fiche_mesures.md`.
- Tu utilises un assistant IA ? D'accord, mais tu dois pouvoir expliquer chaque ligne
  et sa complexité. C'est exactement ce qu'on entraîne dans l'exercice 4.

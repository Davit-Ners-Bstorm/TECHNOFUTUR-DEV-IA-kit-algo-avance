# Fiche de mesures — J5

## 1. BPE

Avec 3 fusions sur « bas bas bas basse basse lasse lasse las », quelles fusions sont apprises ? ……

Comment est découpé « tasse », un mot jamais vu ? ……

## 2. Moteur (`uv run python -m j5.moteur.evaluer`)

| Mesure | Valeur |
|---|---|
| precision@1 | |
| rappel@3 | |
| Question ratée (s'il y en a) et pourquoi | |
| Score obtenu pour la question piège « vacances » | |

## 3. Passage à l'échelle (`uv run python -m j5.moteur.passage_echelle`)

| Sondes | ms / question | Accélération | Rappel@10 |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 4 | | | |
| 8 | | | |

Quel nombre de sondes choisiriez-vous pour un moteur de FAQ ? Et pour un moteur de recherche juridique ? Pourquoi ? ……

## 4. Démos du formateur

| Démo | Mesure |
|---|---|
| `j5.demos.flux_demo` : erreur de HyperLogLog sur 500 000 distincts, mémoire | |
| `j5.demos.vers_numpy` : boucles Python contre NumPy | |

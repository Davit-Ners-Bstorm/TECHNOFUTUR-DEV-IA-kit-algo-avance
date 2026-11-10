# Fiche de mesures — J3

## 1. Démos

| Démo | Mesure | Observation |
|---|---|---|
| `uv run python -m j3.demos.fibonacci` | appels de fib_naif(30) | |
| | temps de fib_memo(500) | |
| `uv run python -m j3.demos.sac_a_dos` | force brute pour 26 objets | |
| | DP pour 200 objets | |

## 2. Déduplication (`uv run python -m j3.dedup.evaluer`)

| Réglage | Comparaisons | Trouvées | Précision | Rappel | Temps |
|---|---|---|---|---|---|
| clé = code postal + 1re lettre du nom, seuil 0.85 | | | | | |
| seuil 0.75 | | | | | |
| seuil 0.95 | | | | | |
| votre propre clé de bloc : …… | | | | | |

Pourquoi le rappel n'atteint-il jamais 100 % avec cette clé de bloc ? ……

Pourquoi la précision n'atteint-elle jamais 100 % ? (pensez aux homonymes) ……

Quelle donnée supplémentaire améliorerait le résultat ? Est-elle nécessaire au regard du RGPD (minimisation) ? ……

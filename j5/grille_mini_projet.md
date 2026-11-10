# Grille d'auto-évaluation — Mini-projet « moteur de recherche sémantique minimal »

Évaluation formative : pas de note. Pour chaque critère, cochez le niveau atteint et donnez la preuve
(commande, chiffre, extrait de code). La présentation au groupe dure 5 minutes par binôme.

| Critère | Débutant | Atteint | Avancé | Preuve |
|---|---|---|---|---|
| **Exactitude** | quelques tests verts | `uv run pytest j5/moteur` tout vert | + tests ajoutés par vous | |
| **Qualité de recherche** | résultats plausibles | précision@1 ≥ 80 %, rappel@3 ≥ 90 % (`evaluer.py`) | analyse d'une question ratée et piste d'amélioration | |
| **Complexité** | ça fonctionne | top-k avec un tas, cosinus sur le plus petit dict | complexité de l'indexation et d'une recherche expliquée en O(…) | |
| **Passage à l'échelle** | IndexExact écrit | IndexIVF écrit, tableau sondes / rappel / vitesse rempli | choix argumenté du nombre de sondes | |
| **Sécurité et RGPD** | filtre d'accès présent | filtre AVANT le classement, longueur de question bornée | autre risque identifié (injection dans les documents, fuite par les scores…) | |
| **Bonus flux** | — | Bloom ou réservoir vert | les deux, et usage dans l'ingestion expliqué | |

## Les trois questions de la présentation

1. Montrez une recherche réussie et une recherche ratée. Pourquoi la seconde échoue-t-elle ?
2. Avec 10 millions de documents, qu'est-ce qui casse en premier dans votre code ? Que changeriez-vous ?
3. Quel est le risque de sécurité ou de vie privée le plus sérieux de votre moteur, et comment le traitez-vous ?

# Grille d'audit de code généré par IA

Cette grille sert tous les jours de la formation. Un code généré par IA est un code
écrit par un collègue pressé et très sûr de lui : on le relit comme tel.

Pour chaque problème trouvé : **ligne**, **catégorie**, **gravité** (bloquant / majeur / mineur),
**preuve** (un test, une mesure ou un exemple d'entrée qui le montre).

| # | Ligne | Catégorie | Problème | Gravité | Preuve |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

## Catégories à passer en revue

1. **Complexité** — boucle cachée (`in` sur une liste, `list.pop(0)`, `sorted` dans une boucle, concaténation de listes). Que se passe-t-il avec 1 million de lignes ?
2. **Cas limites** — entrée vide, un seul élément, doublons, majuscules et espaces, valeurs négatives, `None`.
3. **Exactitude** — le code fait-il ce qui est DEMANDÉ, ou seulement ce qui est TESTÉ ?
4. **Pièges Python** — argument par défaut mutable, effets de bord, variable globale.
5. **Sécurité** — expression régulière vulnérable (ReDoS), entrée non validée, exception qui fuit.
6. **Données personnelles (RGPD)** — données personnelles dans les logs ou la console, données conservées sans raison.

## Questions de conclusion

- Le test fourni par l'IA prouvait-il quelque chose ? Pourquoi est-il passé ?
- Quel test aurait détecté chacun des problèmes ?
- Quelle consigne aurait-il fallu donner à l'assistant IA pour obtenir un meilleur code du premier coup ?

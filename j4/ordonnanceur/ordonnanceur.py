"""LAB J4 (partie 1) — Un ordonnanceur de pipeline, comme ceux des orchestrateurs de données
et des workflows d'agents IA.

Format : taches = {nom: [noms des tâches dont elle dépend]}
         « joindre: [pseudonymiser, agreger_logs] » : joindre ne démarre qu'après ces deux-là.

Interdit : graphlib (la bibliothèque standard le fait déjà : c'est votre oracle dans les tests).

    uv run pytest j4/ordonnanceur
    uv run python -m j4.ordonnanceur.planifier
"""


class CycleError(Exception):
    """Levée quand les dépendances forment un cycle. self.cycle contient le cycle trouvé."""
    def __init__(self, cycle: list):
        super().__init__(" → ".join(map(str, cycle)))
        self.cycle = cycle


def tri_topologique(taches: dict[str, list[str]]) -> list[str]:
    """Un ordre d'exécution où chaque tâche vient après toutes ses dépendances.

    Algorithme de Kahn : compter les dépendances restantes de chaque tâche, démarrer avec
    celles qui n'en ont aucune, et « libérer » leurs successeurs au fur et à mesure.
    S'il reste des tâches jamais libérées : il y a un cycle → lever CycleError(trouver_cycle(taches)).
    Une dépendance qui n'est pas une clé (tâche externe) est considérée comme sans dépendance.
    """
    raise NotImplementedError


def trouver_cycle(taches: dict[str, list[str]]) -> list[str] | None:
    """Un cycle sous forme [a, b, c, a] (premier = dernier), ou None.

    Indice : DFS en trois couleurs. Blanc = pas vu, gris = en cours d'exploration,
    noir = terminé. Retomber sur un sommet GRIS, c'est avoir trouvé un cycle.
    """
    raise NotImplementedError


def niveaux(taches: dict[str, list[str]]) -> list[list[str]]:
    """Les tâches regroupées par vagues exécutables EN PARALLÈLE : niveau 0 = aucune dépendance,
    niveau k = tâches dont toutes les dépendances sont dans les niveaux < k. Chaque vague triée par nom."""
    raise NotImplementedError


def chemin_critique(pipeline: dict[str, tuple[int, list[str]]]) -> tuple[int, list[str]]:
    """Avec des machines en nombre illimité, durée totale minimale du pipeline, et la chaîne de tâches
    qui l'impose (le chemin critique), de la première à la dernière.

    pipeline = {nom: (durée, dépendances)}. C'est un plus LONG chemin dans un graphe sans cycle :
    programmation dynamique dans l'ordre topologique (lien avec le J3).
    """
    raise NotImplementedError

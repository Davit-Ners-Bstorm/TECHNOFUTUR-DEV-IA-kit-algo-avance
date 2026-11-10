"""Tests J4 — ordonnanceur. Oracle : graphlib.TopologicalSorter de la bibliothèque standard."""
import graphlib

import pytest
from hypothesis import given, strategies as st

from j4.donnees_graphes import PIPELINE

DEPS = {t: d for t, (_, d) in PIPELINE.items()}


def respecte_dependances(ordre, taches):
    pos = {t: i for i, t in enumerate(ordre)}
    return all(pos[d] < pos[t] for t, deps in taches.items() for d in deps)


def test_tri_pipeline(od):
    ordre = od.tri_topologique(DEPS)
    assert sorted(ordre) == sorted(DEPS) and respecte_dependances(ordre, DEPS)


def test_tri_dependance_externe(od):
    ordre = od.tri_topologique({"b": ["a"]})        # « a » n'est pas une clé
    assert ordre == ["a", "b"]


# DAG aléatoire : une tâche ne dépend que de tâches de numéro plus petit → jamais de cycle
DAG = st.integers(1, 15).flatmap(lambda n: st.fixed_dictionaries(
    {i: st.lists(st.integers(0, max(i - 1, 0)), max_size=3).map(lambda l, i=i: [x for x in l if x < i])
     for i in range(n)}))


@given(DAG)
def test_tri_comme_graphlib(od, taches):
    ordre = od.tri_topologique(taches)
    list(graphlib.TopologicalSorter(taches).static_order())   # l'oracle ne lève pas d'erreur non plus
    assert sorted(ordre) == sorted(taches) and respecte_dependances(ordre, taches)


def test_cycle_detecte(od):
    taches = {"a": ["c"], "b": ["a"], "c": ["b"], "d": []}
    with pytest.raises(od.CycleError) as e:
        od.tri_topologique(taches)
    cycle = e.value.cycle
    assert cycle[0] == cycle[-1] and set(cycle) == {"a", "b", "c"}


@given(DAG, st.data())
def test_trouver_cycle(od, taches, data):
    assert od.trouver_cycle(taches) is None
    if len(taches) >= 2:
        a, b = data.draw(st.integers(0, len(taches) - 1)), data.draw(st.integers(0, len(taches) - 1))
        taches[min(a, b)] = taches[min(a, b)] + [max(a, b)]   # arc « vers l'avant » : peut créer un cycle
        try:
            list(graphlib.TopologicalSorter(taches).static_order())
            cycle_attendu = False
        except graphlib.CycleError:
            cycle_attendu = True
        cycle = od.trouver_cycle(taches)
        assert (cycle is not None) == cycle_attendu
        if cycle:
            assert cycle[0] == cycle[-1]
            assert all(cycle[i + 1] in taches.get(cycle[i], []) for i in range(len(cycle) - 1))


def test_niveaux(od):
    n = od.niveaux(DEPS)
    assert n[0] == ["extraire_boutique", "extraire_crm", "extraire_logs"]
    assert n[-1] == ["publier"]
    assert len(n) == 8


def test_chemin_critique(od):
    duree, chemin = od.chemin_critique(PIPELINE)
    assert duree == 125
    assert chemin == ["extraire_crm", "nettoyer_clients", "dedoublonner", "pseudonymiser",
                      "joindre", "calculer_embeddings", "indexer_vecteurs", "publier"]


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_tri_perf(od):
    taches = {i: [i - 1] if i else [] for i in range(200_000)}
    assert od.tri_topologique(taches)[:3] == [0, 1, 2]

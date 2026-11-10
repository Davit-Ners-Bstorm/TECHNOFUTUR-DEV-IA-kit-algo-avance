"""Tests J4 — plus courts chemins et union-find."""
import pytest
from hypothesis import given, strategies as st

from j4.donnees_graphes import carte_ponderee, grille

GRAPHE_PONDERE = st.dictionaries(st.integers(0, 7), st.lists(st.tuples(st.integers(0, 7), st.integers(1, 9)), max_size=4),
                                 max_size=8)


def force_brute(g, a, b):
    """Plus court chemin par Bellman-Ford : lent mais simple (oracle)."""
    sommets = set(g) | {v for l in g.values() for v, _ in l} | {a, b}
    d = {s: float("inf") for s in sommets}; d[a] = 0
    for _ in range(len(sommets)):
        for s, l in g.items():
            for v, w in l:
                d[v] = min(d[v], d[s] + w)
    return d[b]


def test_dijkstra_carte(ch):
    cout, chemin = ch.dijkstra(carte_ponderee(), "Bruxelles", "Mettet")
    assert cout == 90 and chemin == ["Bruxelles", "Namur", "Mettet"]


def test_dijkstra_meme_sommet_et_inatteignable(ch):
    assert ch.dijkstra({"a": []}, "a", "a") == (0, ["a"])
    assert ch.dijkstra({"a": [], "b": []}, "a", "b") is None


@given(GRAPHE_PONDERE, st.integers(0, 7), st.integers(0, 7))
def test_dijkstra_comme_bellman_ford(ch, g, a, b):
    res = ch.dijkstra(g, a, b)
    attendu = force_brute(g, a, b)
    if attendu == float("inf"):
        assert res is None
    else:
        cout, chemin = res
        assert cout == attendu and chemin[0] == a and chemin[-1] == b
        poids = {(s, v): min(w for vv, w in g[s] if vv == v) for s in g for v, _ in g[s]}
        assert sum(poids[(chemin[i], chemin[i + 1])] for i in range(len(chemin) - 1)) == cout


def test_a_etoile_meme_longueur_que_dijkstra(ch):
    g = grille()
    arrivee = (len(g) - 1, len(g[0]) - 1)
    avec = ch.a_etoile(g, (0, 0), arrivee, heuristique=True)
    sans = ch.a_etoile(g, (0, 0), arrivee, heuristique=False)
    assert avec is not None and avec[0] == sans[0]            # même longueur : heuristique admissible
    assert avec[1] < sans[1]                                    # mais moins de cases explorées


def test_a_etoile_sans_chemin(ch):
    assert ch.a_etoile([".#", "#."], (0, 0), (1, 1)) is None


def test_bonus_grouper(ch):
    try:
        g = ch.grouper([("a", "b"), ("b", "c"), ("x", "y")], elements=["a", "b", "c", "x", "y", "z"])
    except NotImplementedError:
        pytest.skip("bonus non traité")
    assert sorted(map(sorted, g)) == [["a", "b", "c"], ["x", "y"], ["z"]]


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_bonus_grouper_perf(ch):
    try:
        g = ch.grouper([(i, i + 1) for i in range(300_000)])
    except NotImplementedError:
        pytest.skip("bonus non traité")
    assert len(g) == 1

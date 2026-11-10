"""Tests J4 — parcours de graphes."""
import pytest
from hypothesis import given, strategies as st

from j4.donnees_graphes import DEPENDANCES, graphe_aleatoire

PETITS_GRAPHES = st.dictionaries(st.integers(0, 9), st.lists(st.integers(0, 9), max_size=4), max_size=10)


def test_inverser(pc):
    assert pc.inverser({"a": ["b"], "b": [], "c": ["b"]}) == {"a": [], "b": ["a", "c"], "c": []}


def test_atteignables_avec_cycle(pc):
    g = {1: [2], 2: [3], 3: [1], 4: [1]}
    assert pc.atteignables(g, 1) == {1, 2, 3}


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_atteignables_chaine_tres_longue(pc):
    g = {i: [i + 1] for i in range(100_000)}
    assert len(pc.atteignables(g, 0)) == 100_001       # pas de RecursionError


def test_impactes_faille_crypto(pc):
    attendu = {"tls-outil", "jeton-jwt", "serveur-http", "pilote-sql", "cadre-web", "orm-lite", "appli-web"}
    assert pc.impactes(DEPENDANCES, "crypto-base") == attendu


def test_impactes_paquet_isole(pc):
    assert pc.impactes(DEPENDANCES, "analyse-args") == {"outil-cli"}


def test_distances(pc):
    g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": [], "z": []}
    assert pc.distances(g, "a") == {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}


@given(PETITS_GRAPHES, st.integers(0, 9))
def test_distances_coherentes_avec_atteignables(pc, g, depart):
    if depart not in g:
        g[depart] = []
    assert set(pc.distances(g, depart)) == pc.atteignables(g, depart)


def test_chemin_le_plus_court(pc):
    g = {"a": ["b", "x"], "b": ["c"], "c": ["d"], "x": ["d"], "d": []}
    assert pc.chemin_le_plus_court(g, "a", "d") == ["a", "x", "d"]
    assert pc.chemin_le_plus_court(g, "d", "a") is None
    assert pc.chemin_le_plus_court(g, "a", "a") == ["a"]


@given(PETITS_GRAPHES, st.integers(0, 9), st.integers(0, 9))
def test_chemin_longueur_egale_distance(pc, g, a, b):
    g.setdefault(a, [])
    ch = pc.chemin_le_plus_court(g, a, b)
    d = pc.distances(g, a)
    if b in d:
        assert ch is not None and len(ch) - 1 == d[b] and ch[0] == a and ch[-1] == b
        assert all(ch[i + 1] in g.get(ch[i], []) for i in range(len(ch) - 1))
    else:
        assert ch is None


def test_composantes(pc):
    g = {1: [2], 2: [1], 3: [4], 4: [3], 5: []}
    assert sorted(map(sorted, pc.composantes(g))) == [[1, 2], [3, 4], [5]]


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_composantes_perf(pc):
    g = graphe_aleatoire(200_000, degre=2)
    assert sum(len(c) for c in pc.composantes(g)) == 200_000

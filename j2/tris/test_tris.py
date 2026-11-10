"""Tests J2 — recherche et tris. Oracle : sorted() et la recherche linéaire."""
import random

import pytest
from hypothesis import given, strategies as st

from j2 import versions_naives as naif

ENTIERS = st.lists(st.integers(-50, 50), max_size=200)


# ---------------------------------------------------------------- dichotomie
@given(ENTIERS.map(sorted), st.integers(-60, 60))
def test_dichotomie_comme_recherche_lineaire(t, lst, x):
    assert t.recherche_dichotomique(lst, x) == naif.recherche_lineaire(lst, x)


def test_dichotomie_premiere_occurrence(t):
    assert t.recherche_dichotomique([1, 2, 2, 2, 2, 3], 2) == 1


@pytest.mark.perf
@pytest.mark.timeout(1)
def test_dichotomie_perf(t):
    lst = list(range(0, 2_000_000, 2))
    for x in range(0, 200_000, 7):
        t.recherche_dichotomique(lst, x)


# ---------------------------------------------------------------- tris
@pytest.mark.parametrize("nom", ["tri_fusion", "tri_rapide"])
class TestTris:
    @given(lst=ENTIERS)
    def test_comme_sorted(self, t, nom, lst):
        assert getattr(t, nom)(lst) == sorted(lst)

    def test_ne_modifie_pas_l_entree(self, t, nom):
        lst = [3, 1, 2]
        getattr(t, nom)(lst)
        assert lst == [3, 1, 2]

    def test_chaines(self, t, nom):
        assert getattr(t, nom)(["poire", "abricot", "kiwi"]) == ["abricot", "kiwi", "poire"]


def test_tri_fusion_stable(t):
    # Des cartes : on trie sur la valeur seulement. Les couleurs à égalité gardent leur ordre.
    class Carte:
        def __init__(self, v, c): self.v, self.c = v, c
        def __lt__(self, o): return self.v < o.v
    cartes = [Carte(2, "♠"), Carte(1, "♥"), Carte(2, "♥"), Carte(1, "♠")]
    assert [(c.v, c.c) for c in t.tri_fusion(cartes)] == [(1, "♥"), (1, "♠"), (2, "♠"), (2, "♥")]


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_tri_fusion_perf(t):
    t.tri_fusion([random.random() for _ in range(200_000)])


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_tri_rapide_liste_deja_triee(t):
    t.tri_rapide(list(range(200_000)))


@pytest.mark.perf
@pytest.mark.timeout(3)
def test_tri_rapide_beaucoup_de_doublons(t):
    t.tri_rapide([random.randint(0, 3) for _ in range(200_000)])


# ---------------------------------------------------------------- top_k
@given(ENTIERS, st.integers(0, 20))
def test_top_k_comme_sorted(t, lst, k):
    assert t.top_k(lst, k) == sorted(lst, reverse=True)[:k]


def test_top_k_accepte_un_iterateur(t):
    assert t.top_k(iter([5, 1, 9, 3]), 2) == [9, 5]


@pytest.mark.perf
@pytest.mark.timeout(2)
def test_top_k_perf(t):
    t.top_k((random.random() for _ in range(1_000_000)), 10)


# ---------------------------------------------------------------- bonus
@given(st.lists(ENTIERS.map(sorted), max_size=8))
def test_bonus_fusion_k_listes(t, listes):
    try:
        res = t.fusion_k_listes(listes)
    except NotImplementedError:
        pytest.skip("bonus non traité")
    assert res == sorted(x for l in listes for x in l)

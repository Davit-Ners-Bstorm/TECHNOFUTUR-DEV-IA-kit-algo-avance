"""Tests J5 — mini-projet moteur de recherche."""
import math

import pytest
from hypothesis import given, strategies as st

from j5.corpus import DOCUMENTS, QUESTIONS
from j5.moteur.donnees_vecteurs import generer, questions

TOUS_LES_GROUPES = {"tous", "rh", "securite"}


# ---------------------------------------------------------------- vecteurs
def test_tokens(vec):
    assert vec.tokens("J'ai oublié mon Mot-de-passe !") == ["oublie", "mot", "passe"]


def test_caracteristiques(vec):
    c = vec.caracteristiques("congé")
    assert c == ["conge", "#co", "con", "ong", "nge", "ge#"]


def test_idf_rare_pese_plus(vec):
    w = vec.idf([["a", "b"], ["a"], ["a", "c"]])
    assert w["b"] > w["a"] and w["b"] == w["c"]


def test_vectoriser_normalise(vec):
    v = vec.vectoriser(["a", "a", "b", "inconnu"], {"a": 1.0, "b": 2.0})
    assert "inconnu" not in v
    assert math.isclose(sum(x * x for x in v.values()), 1.0)
    assert vec.vectoriser(["inconnu"], {"a": 1.0}) == {}


@given(st.dictionaries(st.sampled_from("abcdef"), st.floats(0.01, 10), max_size=6),
       st.dictionaries(st.sampled_from("abcdef"), st.floats(0.01, 10), max_size=6))
def test_cosinus(vec, u, v):
    c = vec.cosinus(u, v)
    assert -1e-9 <= c <= 1 + 1e-9
    assert math.isclose(c, vec.cosinus(v, u))
    if u:
        assert math.isclose(vec.cosinus(u, u), 1.0)


# ---------------------------------------------------------------- moteur
@pytest.fixture(scope="module")
def m(mot):
    return mot.Moteur(DOCUMENTS)


def test_qualite(mot, m):
    r = mot.evaluer(m, QUESTIONS, TOUS_LES_GROUPES)
    assert r["precision@1"] >= 0.8 and r["rappel@3"] >= 0.9


def test_resultats_tries_et_positifs(m):
    res = m.rechercher("mot de passe oublié", 5, TOUS_LES_GROUPES)
    scores = [s for _, s in res]
    assert scores == sorted(scores, reverse=True) and all(s > 0 for s in scores)


def test_controle_d_acces(m):
    res = m.rechercher("Grille des salaires par fonction", 3, {"tous"})
    assert "D21" not in [i for i, _ in res]
    assert len(res) == 3                             # les places sont prises par des documents autorisés


def test_controle_d_acces_aucun_document_interdit(m):
    interdits = {d[0] for d in DOCUMENTS if not d[3] & {"tous"}}
    for q, _ in QUESTIONS:
        assert not {i for i, _ in m.rechercher(q, 5, {"tous"})} & interdits


def test_question_trop_longue(m):
    with pytest.raises(ValueError):
        m.rechercher("a" * 501)


# ---------------------------------------------------------------- index
@pytest.fixture(scope="module")
def donnees():
    v = generer(n=3_000)
    return v, questions(v, n=15)


def test_index_exact(idx):
    vecs = [[1.0, 0.0], [0.0, 1.0], [0.7071, 0.7071]]
    assert idx.IndexExact(vecs).rechercher([1.0, 0.0], 2) == [0, 2]


@pytest.mark.perf
@pytest.mark.timeout(20)
def test_ivf_rappel(idx, donnees):
    vecs, qs = donnees
    exact = idx.IndexExact(vecs)
    ivf = idx.IndexIVF(vecs, n_listes=16, iterations=3)
    toutes = [ivf.rechercher(q, 10, n_sondes=16) for q in qs]
    assert toutes == [exact.rechercher(q, 10) for q in qs]        # toutes les listes = recherche exacte
    rappel = sum(idx.rappel_a_k(ivf.rechercher(q, 10, 4), exact.rechercher(q, 10)) for q in qs) / len(qs)
    assert rappel >= 0.6, f"rappel@10 avec 4 sondes sur 16 : {rappel:.0%}"

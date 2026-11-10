"""Tests J3 — déduplication."""
import pytest
from hypothesis import given, strategies as st

from j3 import versions_naives as naif
from j3.dedup.donnees_clients import generer

COURTES = st.text(alphabet="abcd", max_size=6)


# ---------------------------------------------------------------- normaliser
@pytest.mark.parametrize("entree, attendu", [
    ("  Jean-Pierre  DUPONT ", "jean pierre dupont"),
    ("Élodie D'Hondt", "elodie d hondt"),
    ("Noël", "noel"), ("", ""), ("ÇA", "ca"),
])
def test_normaliser(dd, entree, attendu):
    assert dd.normaliser(entree) == attendu


# ---------------------------------------------------------------- levenshtein
@pytest.mark.parametrize("a, b, d", [("chat", "chats", 1), ("kitten", "sitting", 3), ("", "abc", 3),
                                     ("dupont", "dupond", 1), ("peeters", "pieters", 1), ("abc", "abc", 0)])
def test_levenshtein_exemples(dd, a, b, d):
    assert dd.levenshtein(a, b) == d


@given(COURTES, COURTES)
def test_levenshtein_comme_la_definition_recursive(dd, a, b):
    assert dd.levenshtein(a, b) == naif.levenshtein_recursif(a, b)


@given(COURTES, COURTES, COURTES)
def test_levenshtein_est_une_distance(dd, a, b, c):
    assert dd.levenshtein(a, b) == dd.levenshtein(b, a)
    assert dd.levenshtein(a, c) <= dd.levenshtein(a, b) + dd.levenshtein(b, c)   # inégalité triangulaire


@pytest.mark.perf
@pytest.mark.timeout(2)
def test_levenshtein_chaines_longues(dd):
    assert dd.levenshtein("a" * 600, "b" * 600) == 600


# ---------------------------------------------------------------- similarite
def test_similarite(dd):
    assert dd.similarite("", "") == 1.0
    assert dd.similarite("abcd", "abcd") == 1.0
    assert dd.similarite("abcd", "wxyz") == 0.0
    assert dd.similarite("dupont", "dupond") == pytest.approx(5 / 6)


# ---------------------------------------------------------------- doublons
def test_doublons_mini_fichier(dd):
    clients = [
        {"id": "a", "prenom": "Jean-Pierre", "nom": "Dupont", "code_postal": "5000"},
        {"id": "b", "prenom": "JEAN PIERRE", "nom": "DUPONT", "code_postal": "5000"},
        {"id": "c", "prenom": "Jean-Piere", "nom": "Dupont", "code_postal": "5000"},
        {"id": "d", "prenom": "Marie", "nom": "Peeters", "code_postal": "1000"},
        {"id": "e", "prenom": "Luc", "nom": "Lambert", "code_postal": "5000"},
    ]
    assert dd.doublons_probables(clients, 0.85) == {("a", "b"), ("a", "c"), ("b", "c")}


@pytest.mark.perf
@pytest.mark.timeout(5)
def test_doublons_qualite_et_temps(dd):
    clients, verite = generer()
    m = dd.evaluer(dd.doublons_probables(clients, 0.85), verite)
    assert m["rappel"] >= 0.75, f"rappel trop faible : {m['rappel']:.1%}"
    assert m["precision"] >= 0.75, f"précision trop faible : {m['precision']:.1%}"

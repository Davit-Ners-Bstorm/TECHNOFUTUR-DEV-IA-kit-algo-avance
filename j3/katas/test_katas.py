"""Tests J3 — katas récursifs."""
import itertools
import sys

import pytest
from hypothesis import given, strategies as st


# ---------------------------------------------------------------- socle
@given(st.integers(0, 10**12))
def test_somme_chiffres(k, n):
    assert k.somme_chiffres(n) == sum(int(c) for c in str(n))


@pytest.mark.parametrize("entree, attendu", [
    ([], []), ([1, 2], [1, 2]), ([1, [2, [3, 4]], 5], [1, 2, 3, 4, 5]), ([[[]]], []), ([[["a"]], "b"], ["a", "b"]),
])
def test_aplatir(k, entree, attendu):
    assert k.aplatir(entree) == attendu


@given(st.integers(-5, 5), st.integers(0, 60))
def test_puissance_rapide(k, x, n):
    assert k.puissance_rapide(x, n) == x ** n


def test_puissance_rapide_logarithmique(k):
    class Compteur(int):
        mult = 0
        def __mul__(self, o):
            Compteur.mult += 1
            return Compteur(int(self) * int(o))
        __rmul__ = __mul__
    k.puissance_rapide(Compteur(1), 1_000_000)
    assert Compteur.mult < 100, f"{Compteur.mult} multiplications : ce n'est pas O(log n)"


# ---------------------------------------------------------------- standard
def test_taille_dossier(k):
    arbre = {"nom": "projet", "taille": 4, "enfants": [
        {"nom": "src", "taille": 10, "enfants": [{"nom": "main.py", "taille": 3, "enfants": []}]},
        {"nom": "README", "taille": 1},
    ]}
    assert k.taille_dossier(arbre) == 18


@given(st.lists(st.integers(1, 30), max_size=12), st.integers(0, 120))
def test_sous_ensemble_somme(k, nombres, cible):
    res = k.sous_ensemble_somme(nombres, cible)
    existe = any(sum(c) == cible for r in range(len(nombres) + 1)
                 for c in itertools.combinations(nombres, r))
    if existe:
        assert res is not None and sum(res) == cible
        reste = list(nombres)
        for x in res:
            reste.remove(x)            # chaque nombre utilisé au plus une fois
    else:
        assert res is None


@given(st.lists(st.integers(0, 9), max_size=6))
def test_permutations(k, elements):
    res = k.permutations(elements)
    assert sorted(map(tuple, res)) == sorted(itertools.permutations(elements))


# ---------------------------------------------------------------- bonus
@pytest.mark.parametrize("n, attendu", [(1, 1), (4, 2), (6, 4), (8, 92)])
def test_bonus_n_reines(k, n, attendu):
    try:
        assert k.n_reines(n) == attendu
    except NotImplementedError:
        pytest.skip("bonus non traité")


def test_bonus_profondeur_tres_profonde(k):
    v = []
    for _ in range(100_000):
        v = [v]
    limite = sys.getrecursionlimit()
    try:
        assert k.profondeur(v) == 100_001
        assert k.profondeur(5) == 0 and k.profondeur([[1], 2]) == 2 and k.profondeur([]) == 1
    except NotImplementedError:
        pytest.skip("bonus non traité")
    assert sys.getrecursionlimit() == limite, "ne pas modifier la limite de récursion"

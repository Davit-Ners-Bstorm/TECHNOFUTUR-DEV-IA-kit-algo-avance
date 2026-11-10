"""Tests J5 — bonus algorithmes de flux."""
from collections import Counter

import pytest


def _ou_skip(f, *a):
    try:
        return f(*a)
    except NotImplementedError:
        pytest.skip("bonus non traité")


@pytest.fixture(scope="module")
def fl():
    from outils.choix import charger
    return charger("j5.flux.flux")


def test_bloom_aucun_faux_negatif(fl):
    b = _ou_skip(fl.FiltreBloom, 20_000, 5)
    vus = [f"doc-{i}" for i in range(2_000)]
    for x in vus:
        b.ajouter(x)
    assert all(b.contient(x) for x in vus)


def test_bloom_peu_de_faux_positifs(fl):
    b = _ou_skip(fl.FiltreBloom, 20_000, 5)
    for i in range(2_000):
        b.ajouter(f"doc-{i}")
    faux = sum(b.contient(f"autre-{i}") for i in range(10_000))
    assert faux / 10_000 < 0.02                 # théorie : ≈ 0,9 % pour 10 bits par élément et 5 hachages


def test_bloom_compact(fl):
    b = _ou_skip(fl.FiltreBloom, 80_000, 3)
    assert len(b.bits) <= 10_000


def test_reservoir_taille_et_contenu(fl):
    e = _ou_skip(fl.echantillon_reservoir, iter(range(1_000)), 10)
    assert len(e) == 10 and len(set(e)) == 10 and all(0 <= x < 1_000 for x in e)
    assert _ou_skip(fl.echantillon_reservoir, iter(range(3)), 10) == [0, 1, 2]


def test_reservoir_uniforme(fl):
    compte = Counter()
    for g in range(2_000):
        compte.update(_ou_skip(fl.echantillon_reservoir, iter(range(20)), 5, g))
    # chaque élément devrait sortir ≈ 2 000 × 5 / 20 = 500 fois
    assert all(400 < compte[x] < 600 for x in range(20))

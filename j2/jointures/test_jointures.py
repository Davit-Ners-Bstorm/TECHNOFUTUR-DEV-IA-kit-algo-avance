"""Tests J2 — jointures. Oracle : la jointure par boucles imbriquées, puis SQLite."""
import sqlite3

import pytest
from hypothesis import given, strategies as st

from j2 import versions_naives as naif
from j2.jointures import donnees_jointure as dj

# Petites tables générées : ids entre 0 et 5 → beaucoup de collisions, doublons et None
CLIENTS = st.lists(st.tuples(st.one_of(st.none(), st.integers(0, 5)), st.sampled_from("ABC"),
                             st.just("Namur")), max_size=8)
COMMANDES = st.lists(st.tuples(st.integers(1, 99), st.one_of(st.none(), st.integers(0, 6)),
                               st.floats(1, 100, allow_nan=False)), max_size=12)

FONCTIONS = ["jointure_hachage", "jointure_tri_fusion"]


@pytest.mark.parametrize("nom", FONCTIONS)
class TestJointures:
    def test_exemple(self, j, nom):
        clients = [(1, "Alice", "Namur"), (2, "Bruno", "Mons")]
        commandes = [(10, 2, 50.0), (11, 1, 20.0), (12, 3, 9.0), (13, None, 1.0)]
        assert sorted(getattr(j, nom)(clients, commandes)) == [(10, "Bruno", 50.0), (11, "Alice", 20.0)]

    def test_cle_en_double_des_deux_cotes(self, j, nom):
        clients = [(1, "A", "x"), (1, "B", "x")]          # id 1 en double : données sales
        commandes = [(10, 1, 5.0), (11, 1, 6.0)]
        assert len(getattr(j, nom)(clients, commandes)) == 4

    def test_none_ne_correspond_a_rien(self, j, nom):
        assert getattr(j, nom)([(None, "X", "v")], [(1, None, 1.0)]) == []

    @given(clients=CLIENTS, commandes=COMMANDES)
    def test_comme_boucles_imbriquees(self, j, nom, clients, commandes):
        attendu = sorted(naif.jointure_boucles(clients, commandes))
        assert sorted(getattr(j, nom)(clients, commandes)) == attendu

    def test_comme_sqlite(self, j, nom):
        cli, cmd = dj.clients(500), dj.commandes(3_000, 500)
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE clients(id INTEGER, nom TEXT, ville TEXT)")
        con.execute("CREATE TABLE commandes(id INTEGER, client_id INTEGER, montant REAL)")
        con.executemany("INSERT INTO clients VALUES (?, ?, ?)", cli)        # requêtes paramétrées
        con.executemany("INSERT INTO commandes VALUES (?, ?, ?)", cmd)
        sql = sorted(con.execute("SELECT cmd.id, cli.nom, cmd.montant FROM commandes cmd "
                                 "JOIN clients cli ON cmd.client_id = cli.id"))
        assert sorted(getattr(j, nom)(cli, cmd)) == sql

    @pytest.mark.perf
    @pytest.mark.timeout(3)
    def test_perf(self, j, nom):
        getattr(j, nom)(dj.clients(100_000), dj.commandes(500_000, 100_000))


def test_bonus_jointure_gauche(j):
    try:
        res = j.jointure_gauche([(1, "A", "x")], [(10, 1, 5.0), (11, 9, 6.0), (12, None, 1.0)])
    except NotImplementedError:
        pytest.skip("bonus non traité")
    assert sorted(res, key=str) == sorted([(10, "A", 5.0), (11, None, 6.0), (12, None, 1.0)], key=str)

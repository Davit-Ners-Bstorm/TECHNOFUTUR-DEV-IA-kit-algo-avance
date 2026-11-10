"""Tests du lab J1 : d'abord juste, ensuite rapide.

    uv run pytest j1/lab                 tous les tests
    uv run pytest j1/lab -m "not perf"   seulement l'exactitude
"""
import pytest

from j1.lab import versions_naives as naif
from outils import donnees

# Budget de temps des tests « perf ». Une version O(n²) n'a aucune chance de tenir.
BUDGET = 2  # secondes


# ---------------------------------------------------------------- doublons
class TestDoublons:
    def test_exemple(self, s):
        assert s.doublons(["a", "b", "a", "c", "b", "a"]) == ["a", "b"]

    def test_vide_et_sans_doublon(self, s):
        assert s.doublons([]) == []
        assert s.doublons(["a", "b"]) == []

    def test_ordre_de_deuxieme_apparition(self, s):
        assert s.doublons(["x", "y", "y", "x"]) == ["y", "x"]

    def test_comme_la_version_naive(self, s):
        data = donnees.emails(2_000)
        assert s.doublons(data) == naif.doublons(data)

    @pytest.mark.perf
    @pytest.mark.timeout(BUDGET)
    def test_perf(self, s):
        s.doublons(donnees.emails(300_000))


# ---------------------------------------------------------------- paires_somme
class TestPairesSomme:
    @pytest.mark.parametrize("nombres, cible, attendu", [
        ([2, 7, 11, 15], 9, True),
        ([3, 3], 6, True),
        ([3], 6, False),           # un seul élément : pas de paire avec lui-même
        ([1, 2, 3], 7, False),
        ([], 0, False),
        ([-5, 10, 4], 5, True),
    ])
    def test_cas(self, s, nombres, cible, attendu):
        assert s.paires_somme(nombres, cible) is attendu

    @pytest.mark.perf
    @pytest.mark.timeout(BUDGET)
    def test_perf_cas_defavorable(self, s):
        # cible impossible → il faut tout parcourir
        assert s.paires_somme(donnees.nombres(300_000), 10_000_000) is False


# ---------------------------------------------------------------- top_k
class TestTopK:
    def test_exemple(self, s):
        ventes = [("B", 5), ("A", 3), ("C", 1), ("A", 4), ("B", 1)]
        assert s.top_k(ventes, 2) == [("A", 7), ("B", 6)]

    def test_egalite_ordre_alphabetique(self, s):
        assert s.top_k([("Z", 2), ("M", 2), ("A", 1)], 2) == [("M", 2), ("Z", 2)]

    def test_k_plus_grand_que_le_nombre_de_produits(self, s):
        assert s.top_k([("A", 1)], 5) == [("A", 1)]

    def test_comme_la_version_naive(self, s):
        data = donnees.ventes(5_000)
        assert s.top_k(data, 10) == naif.top_k(data, 10)

    @pytest.mark.perf
    @pytest.mark.timeout(BUDGET)
    def test_perf(self, s):
        s.top_k(donnees.ventes(500_000), 10)


# ---------------------------------------------------------------- moyenne_glissante
class TestMoyenneGlissante:
    def test_exemple(self, s):
        assert s.moyenne_glissante([1, 2, 3, 4, 5], 2) == pytest.approx([1.5, 2.5, 3.5, 4.5])

    def test_fenetre_trop_grande(self, s):
        assert s.moyenne_glissante([1, 2], 3) == []

    def test_fenetre_invalide(self, s):
        with pytest.raises(ValueError):
            s.moyenne_glissante([1, 2], 0)

    def test_comme_la_version_naive(self, s):
        data = donnees.mesures_capteur(3_000)
        assert s.moyenne_glissante(data, 50) == pytest.approx(naif.moyenne_glissante(data, 50))

    @pytest.mark.perf
    @pytest.mark.timeout(BUDGET)
    def test_perf_grande_fenetre(self, s):
        s.moyenne_glissante(donnees.mesures_capteur(300_000), 5_000)


# ---------------------------------------------------------------- compter_dans_tranche
class TestTranche:
    @pytest.mark.parametrize("bas, haut, attendu", [
        (2, 4, 4),        # bornes incluses, doublon de 3 compté deux fois
        (0, 100, 6),
        (6, 9, 0),
        (5, 5, 1),
        (4, 2, 0),        # tranche vide
    ])
    def test_cas(self, s, bas, haut, attendu):
        assert s.compter_dans_tranche([1, 2, 3, 3, 4, 5], bas, haut) == attendu

    @pytest.mark.perf
    @pytest.mark.timeout(BUDGET)
    def test_perf_beaucoup_de_requetes(self, s):
        prix = donnees.prix_tries(200_000)
        for i in range(20_000):           # 20 000 requêtes sur la même liste
            s.compter_dans_tranche(prix, i % 900, i % 900 + 50)


# ---------------------------------------------------------------- BONUS tarif
class TestBonusTarif:
    def test_resultat_identique(self, s):
        opts = {"premium": True, "remise": 10}
        assert s.tarif(opts) == s.tarif_lent(dict(opts))

    def test_un_seul_calcul_par_combinaison(self, s):
        s.APPELS["tarif_lent"] = 0
        for _ in range(100):
            s.tarif({"premium": False, "remise": 5})
            s.tarif({"remise": 5, "premium": False})   # même options, autre ordre
        assert s.APPELS["tarif_lent"] == 1

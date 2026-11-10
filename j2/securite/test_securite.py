"""Tests J2 — sécurité algorithmique."""
import hmac

import pytest

from j2 import versions_naives as naif


# ---------------------------------------------------------------- nom_valide
@pytest.mark.parametrize("nom, attendu", [
    ("Jean-Pierre", True), ("O'Brien", True), ("Élodie Van den Broeck", True),
    ("", False), (" Alice", False), ("Alice ", False), ("Al1ce", False),
    ("Robert'); DROP TABLE clients;--", False), ("a" * 100, True), ("a" * 101, False),
])
def test_nom_valide_regles(sec, nom, attendu):
    assert sec.nom_valide(nom) is attendu


@pytest.mark.parametrize("nom", ["Jean-Pierre", "O'Brien", "Anne Marie", "x"])
def test_nom_valide_comme_regex_sur_entrees_normales(sec, nom):
    assert sec.nom_valide(nom) == naif.nom_valide_regex(nom)


@pytest.mark.timeout(1)
def test_nom_valide_resiste_au_redos(sec):
    assert sec.nom_valide("a" * 40 + "!") is False      # la regex mettrait des heures
    assert sec.nom_valide("a" * 1_000_000) is False     # borne de longueur vérifiée d'abord


# ---------------------------------------------------------------- verifier_jeton
def test_jeton_resultats(sec):
    assert sec.verifier_jeton("s3cr3t", "s3cr3t") is True
    assert sec.verifier_jeton("s3cr3t", "s3cr3T") is False
    assert sec.verifier_jeton("é-jeton", "é-jeton") is True     # non ASCII


def test_jeton_utilise_compare_digest(sec, monkeypatch):
    appels = []
    vrai = hmac.compare_digest
    monkeypatch.setattr(hmac, "compare_digest", lambda a, b: appels.append(1) or vrai(a, b))
    sec.verifier_jeton("abc", "abd")
    assert appels, "la comparaison doit passer par hmac.compare_digest"


# ---------------------------------------------------------------- lire_parametres
def test_parametres_normaux(sec):
    assert sec.lire_parametres("ville=Namur&page=2") == {"ville": ["Namur"], "page": ["2"]}


def test_parametres_trop_nombreux(sec):
    with pytest.raises(ValueError):
        sec.lire_parametres("&".join(f"p{i}=1" for i in range(10_000)))

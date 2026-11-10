"""Fixtures du J2. ALGO_CORRIGE=1 teste les corrigés du formateur."""
import pytest

from outils.choix import charger


@pytest.fixture(scope="session")
def t():
    return charger("j2.tris.tris")


@pytest.fixture(scope="session")
def j():
    return charger("j2.jointures.jointures")


@pytest.fixture(scope="session")
def sec():
    return charger("j2.securite.securite")

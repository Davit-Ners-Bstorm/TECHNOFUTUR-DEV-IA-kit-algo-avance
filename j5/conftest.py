"""Fixtures du J5. ALGO_CORRIGE=1 teste les corrigés du formateur."""
import pytest

from outils.choix import charger


@pytest.fixture(scope="session")
def bpe():
    return charger("j5.bpe.bpe")


@pytest.fixture(scope="session")
def vec():
    return charger("j5.moteur.vecteurs")


@pytest.fixture(scope="session")
def idx():
    return charger("j5.moteur.index")


@pytest.fixture(scope="session")
def mot():
    return charger("j5.moteur.moteur")

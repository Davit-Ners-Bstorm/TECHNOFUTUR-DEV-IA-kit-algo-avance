"""Fixtures du J4. ALGO_CORRIGE=1 teste les corrigés du formateur."""
import pytest

from outils.choix import charger


@pytest.fixture(scope="session")
def pc():
    return charger("j4.parcours.parcours")


@pytest.fixture(scope="session")
def od():
    return charger("j4.ordonnanceur.ordonnanceur")


@pytest.fixture(scope="session")
def ch():
    return charger("j4.chemins.chemins")

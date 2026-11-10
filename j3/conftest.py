"""Fixtures du J3. ALGO_CORRIGE=1 teste les corrigés du formateur."""
import pytest

from outils.choix import charger


@pytest.fixture(scope="session")
def k():
    return charger("j3.katas.katas")


@pytest.fixture(scope="session")
def dd():
    return charger("j3.dedup.dedup")

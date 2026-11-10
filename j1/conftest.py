"""Choisit la version testée : la tienne (par défaut) ou le corrigé du formateur.

    uv run pytest j1                      → teste j1/lab/structures.py
    ALGO_CORRIGE=1 uv run pytest j1       → teste corriges/j1/lab/structures.py
"""
import importlib
import os

import pytest


@pytest.fixture(scope="session")
def s():
    nom = "corriges.j1.lab.structures" if os.environ.get("ALGO_CORRIGE") else "j1.lab.structures"
    return importlib.import_module(nom)

"""Charge ta version d'un module, ou le corrigé si ALGO_CORRIGE=1 (réservé au formateur)."""
import importlib
import os


def charger(nom_module: str):
    """charger("j2.tris.tris") → j2/tris/tris.py, ou corriges/j2/tris/tris.py."""
    if os.environ.get("ALGO_CORRIGE"):
        return importlib.import_module("corriges." + nom_module)
    return importlib.import_module(nom_module)

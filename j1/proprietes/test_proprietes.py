"""EXERCICE 3 — Tests par propriétés avec Hypothesis.

Un test classique vérifie UN exemple choisi par toi.
Un test de propriété vérifie une RÈGLE sur des centaines d'entrées générées,
y compris celles auxquelles tu n'aurais pas pensé (liste vide, négatifs, doublons…).

Stratégie de l'oracle : la version naïve est lente mais simple, donc digne de confiance.
On vérifie que ta version rapide donne TOUJOURS le même résultat.

    uv run pytest j1/proprietes
"""
from hypothesis import given, strategies as st

from j1.lab import versions_naives as naif
from j1.lab import structures as opti


# --- EXEMPLE COMPLET -------------------------------------------------------
@given(st.lists(st.integers(-100, 100), max_size=60), st.integers(-200, 200))
def test_paires_somme_comme_oracle(s, nombres, cible):
    assert s.paires_somme(nombres, cible) == naif.paires_somme(nombres, cible)


# --- À TOI ------------------------------------------------------------------
# Remplace chaque `pass` par un test. Supprime le décorateur @skip quand tu commences.
import pytest  # noqa: E402

A_FAIRE = pytest.mark.skip(reason="exercice à compléter")

PETITS_MOTS = st.lists(st.sampled_from(["a", "b", "c", "d"]), max_size=40)

@given(PETITS_MOTS)
def test_doublons_comme_oracle(emails):
    assert naif.doublons(emails) == opti.doublons(emails)


@given(PETITS_MOTS)
def test_doublons_proprietes(emails, s):
    resultat = s.doublons(emails)
    assert len(resultat) == len(set(emails))
    # ['a', 'a', 'b', 'c', 'e', 'e']
    # => resultat = ['a', 'e']

    # et chaque élément du résultat apparaît au moins 2 fois dans l'entrée.
    for res in resultat:
        assert emails.count(res) >= 2


@A_FAIRE
def test_top_k_longueur(s):
    # Propriété : len(résultat) == min(k, nombre de produits distincts).
    pass


@A_FAIRE
def test_tranche_comme_oracle(s):
    # Piège : la liste DOIT être triée. Indice : .map(sorted) sur une stratégie de liste.
    pass


@A_FAIRE
def test_moyenne_glissante_comme_oracle(s):
    # Piège : les flottants. Compare avec pytest.approx, et limite les valeurs
    # (st.floats(-1e6, 1e6, allow_nan=False)). Que se passe-t-il sans ces limites ?
    pass

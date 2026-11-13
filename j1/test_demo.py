from j1.lab.versions_naives import paires_somme as nf_paires_sommes

def my_sum(a, b):
    return a + b

def test_my_sum():
    assert my_sum(2, 2) == 4
    assert my_sum(2, 5) == 7
    assert my_sum(0, 5) == 5




from hypothesis import given, strategies as st
from j1.lab.structures import paires_somme
 
@given(st.lists(st.integers(-100, 100)),
       st.integers(-200, 200))
def test_paires_somme_comme_oracle(nombres, cible):
    rapide = paires_somme(nombres, cible)
    lent = nf_paires_sommes(nombres, cible)
    assert rapide == lent

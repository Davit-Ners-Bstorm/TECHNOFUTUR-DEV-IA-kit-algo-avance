"""Tests J5 — BPE."""
from hypothesis import given, strategies as st

TEXTE = "bas bas bas basse basse lasse lasse las"


def test_compter_paires(bpe):
    p = bpe.compter_paires(bpe.preparer("bas basse"))
    assert p[("b", "a")] == 2 and p[("s", "s")] == 1 and p[("s", "</w>")] == 1


def test_fusionner(bpe):
    c = bpe.fusionner({("a", "a", "a", "</w>"): 1}, ("a", "a"))
    assert c == {("aa", "a", "</w>"): 1}            # de gauche à droite, sans chevauchement


def test_entrainer(bpe):
    f = bpe.entrainer(TEXTE, 3)
    assert f == [("a", "s"), ("b", "as"), ("e", "</w>")]   # égalité 4-4 : ordre alphabétique


def test_tokeniser_mot_inconnu(bpe):
    f = bpe.entrainer(TEXTE, 6)
    assert bpe.tokeniser("lasse", f)[0].startswith("l")
    assert "".join(bpe.tokeniser("tasse", f)).replace("</w>", "") == "tasse"   # rien ne se perd


@given(st.text(alphabet="abcs ", min_size=1, max_size=40), st.integers(0, 10),
       st.text(alphabet="abcsz", min_size=1, max_size=8))
def test_tokeniser_reversible(bpe, texte, n, mot):
    f = bpe.entrainer(texte, n)
    assert "".join(bpe.tokeniser(mot, f)) == mot.lower() + "</w>"


def test_plus_de_fusions_moins_de_tokens(bpe):
    t3 = bpe.tokeniser("basse", bpe.entrainer(TEXTE, 3))
    t8 = bpe.tokeniser("basse", bpe.entrainer(TEXTE, 8))
    assert len(t8) <= len(t3)

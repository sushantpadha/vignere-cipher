import pytest
from vignere_cipher import alphabet, normalize, get_key, encrypt, decrypt

key = "godsavethequeen"
key *= 5  # just to be safe


@pytest.mark.parametrize(
    "letter,num",
    [('a', 0), ('p', 15), ('z', 25)]
)
def test_alphabet(letter, num):
    assert alphabet.index(letter) == num


@pytest.mark.parametrize(
    "text,key,expanded_key",
    [('123', 'bruh', 'bru'),
     ('123456', 'bruh', 'bruhbr'),
     ('123456789', 'bruh', 'bruhbruhb')]
)
def test_get_key(text, key, expanded_key):
    assert get_key(text, key) == expanded_key


@pytest.mark.parametrize(
    "raw,normed",
    [('as df', 'asdf'), ('as1df', 'asdf'), ('as%df', 'asdf')]
)
def test_normalize(raw, normed):
    assert normalize(raw) == normed


@pytest.mark.parametrize(
    "text,encrypted",
    [('comeretribution', 'icpwrzxkpfknmsa'),
     ('phoenixhaslanded', 'vvrwndbahwburhrj'),
     ('attackatdawn', 'ghwscfemkemh')]
)
def test_encrypt(text, encrypted):
    assert encrypt(text) == encrypted


@pytest.mark.parametrize(
    "encrypted,text",
    [('icpwrzxkpfknmsa', 'comeretribution'),
     ('vvrwndbahwburhrj', 'phoenixhaslanded'),
     ('ghwscfemkemh', 'attackatdawn')]
)
def test_decrypt(encrypted, text):
    assert decrypt(encrypted) == text

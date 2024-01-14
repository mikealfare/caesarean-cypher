from typing import List

import pytest

from src.caesarean_cypher.cypher import decode, decode_char


@pytest.mark.parametrize("cypher_char,shift,plain_char", [
    ("a", 1, "z"),
    ("d", 3, "a"),
])
def test_decode_char(cypher_char: str, shift: int, plain_char: str) -> None:
    assert decode_char(cypher_char, shift) == plain_char


@pytest.mark.parametrize("cypher_text,shifts,plain_text", [
    ("abcde", [1, 3], "zybad"),
    ("abc de", [1, 3], "zyb ad"),
    ("aBc, de", [1, 3], "zyb, ad"),
])
def test_decode(cypher_text: str, shifts: List[int], plain_text: str) -> None:
    assert decode(cypher_text, shifts) == plain_text

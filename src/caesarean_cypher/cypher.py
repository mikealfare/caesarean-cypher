from string import ascii_lowercase
from typing import List


def decode_char(char: str, shift: int) -> str:
    cypher_index = ascii_lowercase.find(char)
    plain_index = (cypher_index - shift) % 26
    return ascii_lowercase[plain_index]


def decode(cypher_text: str, shifts: List[int]) -> str:
    plain_text = ""
    shift_index = 0
    for cypher_char in cypher_text:
        if cypher_char.lower() in ascii_lowercase:
            plain_text += decode_char(cypher_char.lower(), shifts[shift_index])
            shift_index = (shift_index + 1) % len(shifts)
        else:
            plain_text += cypher_char
    return plain_text


if __name__ == "__main__":
    message = "ddo'u zbjw up vff bpv pjog jg l cpuspz uih dbu bhdjo? - f"
    shifts = [1, 3, 1]
    print(decode(message, shifts))
    message = "enfxiti. wpwh px wlve qysa ys, dmtosva cobv osh mhr iu xhl aaf - g"
    shifts = [4, 0, 7]
    print(decode(message, shifts))

"""
encrypt and decipher messages with vignere cipher
"""

import argparse

STANDARD_ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"
ASCII_CHARS: str = r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


class KeyGen:
    def __init__(self, key: str, length: int, alphabet: str) -> None:
        self.key: str = key
        self.length: int = length
        self.alphabet: str = alphabet

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        key = self.key
        key_len = len(key)
        if self._idx >= self.length:
            raise StopIteration
        shift = self.alphabet.index(key[self._idx % key_len])
        self._idx += 1
        return shift


def check_key(key: str, alphabet: str):
    for i, c in enumerate(key):
        if c not in alphabet:
            raise ValueError(
                f"key: '{key}' is not valid since it contains invalid character '{c}' at index {i}"
            )
    return


def encrypt(
    plaintext: str, key_gen: KeyGen, decrypt: bool, alphabet: str, extended: bool
):
    encrypted = []
    key_gen_iter = iter(key_gen)
    alphabet_length = len(alphabet)
    for c in plaintext:
        c_wasupper = c.isupper()
        c = c if extended else c.lower()
        c_i = alphabet.find(c)
        # if c is not in alphabet
        if c_i == -1:
            encrypted.append(c)
        else:
            shift = next(key_gen_iter)
            shift = -(shift) if decrypt else shift
            new_c_i = (c_i + shift) % alphabet_length
            new_c = alphabet[new_c_i]
            new_c = new_c.upper() if (c_wasupper and not extended) else new_c
            encrypted.append(new_c)

    return "".join(encrypted)


def main(args=None):
    namespace = parse_args(args)
    parsed_vars = vars(namespace)
    text = parsed_vars["text"]
    key = parsed_vars["key"]
    d = parsed_vars["d"]
    extended = parsed_vars["extended"]

    alphabet = ASCII_CHARS if extended else STANDARD_ALPHABET

    check_key(key, alphabet)
    key_gen = KeyGen(key, len(text), alphabet)

    r = encrypt(text, key_gen, d, alphabet, extended)

    print(r)

    return


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="\x1b[3m“Sometimes it’s the people no one "
        + "imagines anything of who do the things "
        + "that no one can imagine.”\x1b[0m",
    )
    parser.add_argument(
        "text",
        action="store",
        help="text message to decrypt or encrypt "
        + "\nstandard mode: non-alphabetic characters and cases of alphabetic characters will be preserved"
        + "\nextended mode: all characters will be en/decrypted according to extended alphabet, non-ascii characters will be preserved",
    )
    parser.add_argument(
        "-k",
        action="store",
        dest="key",
        required=True,
        help="key to use to en/decrypt text "
        + "case is preserved (if applicable) and non-alphabet characters are preserved",
    )
    action = parser.add_mutually_exclusive_group()
    action.add_argument(
        "-e", action="store_true", dest="e", help="encrypt text using key"
    )
    action.add_argument(
        "-d", action="store_true", dest="d", help="decrypt text using key"
    )
    parser.add_argument(
        "--extended",
        action="store_true",
        dest="extended",
        required=False,
        help="use extended alphabet consisting of all ascii characters from 33 to 126. prefer using raw strings",
    )
    return parser.parse_args(args=args)


if __name__ == "__main__":
    main()

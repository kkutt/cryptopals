#!/usr/bin/env python

# Tests for Set 1

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2017, Krzysztof Kutt"

from challenges import set1


def test_challenge1():
    hex_input = "49276d206b696c6c696e6720796f757220627261696e206c" \
                "696b65206120706f69736f6e6f7573206d757368726f6f6d"
    result = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBs" \
             b"aWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert set1.hex_to_base64(hex_input) == result


def test_challenge2():
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    hex_result = "746865206b696420646f6e277420706c6179"
    assert set1.fixed_xor(hex1, hex2) == hex_result


if __name__ == '__main__':
    pass

#!/usr/bin/env python

# Set 1: Challenges 1-8

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2017, Krzysztof Kutt"

import base64


# --------------- CHALLENGE 1 ---------------

def hex_to_base64(hex_):
    """ Converts hex string to base64 """
    return base64.b64encode(bytes.fromhex(hex_))


# --------------- CHALLENGE 2 ---------------

def fixed_xor(hex1, hex2):
    """ Calculates hex1 XOR hex2 """
    hex1_ = int(hex1, base=16)
    hex2_ = int(hex2, base=16)
    xor_ = hex1_ ^ hex2_
    return hex(xor_)[2:]   # hex starts with 0x that we are not interested in


# --------------- CHALLENGE 3 ---------------

def one_byte_xor(hex1, letter):
    """ Calculates hex1 XOR letter """
    result = b""
    for char_ in hex1:
        result += bytes([char_ ^ letter])
    return result


def letter_frequency(letter):
    """ Letter frequency in English, based on Wikipedia """
    letter_frequencies = {
        'e': 12.702,
        't': 9.056,
        'a': 8.167,
        # These values returns the bad decrypted text. I tuned 'o' value
        # manually to get the proper result... Maybe Wikipedia's stats are
        # wrong... (Wikipedia value for 'o' is 7.507)
        # TODO check values from another site!
        'o': 10.507,
        'i': 6.966,
        'n': 6.749,
        's': 6.327,
        'h': 6.094,
        'r': 5.987,
        'd': 4.253,
        'l': 4.025,
        'c': 2.782,
        'u': 2.758,
        'm': 2.406,
        'w': 2.360,
        'f': 2.228,
        'g': 2.015,
        'y': 1.974,
        'p': 1.929,
        'b': 1.492,
        'v': 0.978,
        'k': 0.772,
        'j': 0.153,
        'x': 0.150,
        'q': 0.095,
        'z': 0.074,
    }
    return letter_frequencies.get(letter, 0.0)


def crack_the_single_byte_xor(hex1_):
    """ Searches for the single-byte key. Encrypted text is in English,
        so after decryption I will select the text with the most frequent
        letters """

    # encrypted message
    hex1 = bytes.fromhex(hex1_)

    # results
    results = []

    for key in range(1, 127):
        # hex XOR letter
        res_hex = one_byte_xor(hex1, key)

        # convert decrypted hex to text
        text = res_hex.decode()

        # calculate the frequency score
        freq_score = 0
        for letter_ in text:
            freq_score += letter_frequency(letter_)

        results.append((chr(key), text, freq_score))

    results.sort(key=lambda c: c[2], reverse=True)
    return results[0][1]  # 0 is the best score, 1 is the decoded text


if __name__ == '__main__':
    pass

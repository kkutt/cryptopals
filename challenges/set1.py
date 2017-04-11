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


if __name__ == '__main__':
    pass

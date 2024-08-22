#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding

    Prototype: def validUTF8(data)

    Return: True if data is a valid UTF-8 encoding, else return False
    """

    bytes_n = 0
    bytes_1 = 1 << 7
    bytes_2 = 1 << 6

    for byte in data:
        byte_n = 1 << 7
        if bytes_n == 0:
            while byte & byte_n:
                bytes_n += 1
                byte_n = byte_n >> 1
            if bytes_n == 0:
                continue
            if bytes_n == 1 or bytes_n > 4:
                return False
        else:
            if not (byte & bytes_1 and not (byte & bytes_2)):
                return False
        bytes_n -= 1
    return bytes_n == 0

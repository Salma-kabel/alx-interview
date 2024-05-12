#!/usr/bin/python3
"""method that determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """True if data is a valid UTF-8 encoding, else return False"""
    i = 0
    t = 1
    while i < len(data):
        if (data[i] & 0xf0) == 0xf0:
            if i + 1 < len(data) and i + 2 < len(data) and i + 3 < len(data)\
            and (data[i + 1] & 0x80) == 0x80 and (data[i + 2] & 0x80) == 0x80\
            and (data[i + 3] & 0x80) == 0x80:
                t = 1
                i += 4
            else:
                t = 0
                break
        elif (data[i] & 0xe0) == 0xe0:
            if i + 1 < len(data) and i + 2 < len(data) and\
            (data[i + 1] & 0x80) == 0x80 and (data[i + 2] & 0x80) == 0x80:
                t = 1
                i += 3
            else:
                t = 0
                break
        elif (data[i] & 0xc0) == 0xc0:
            if i + 1 < len(data) and (data[i + 1] & 0x80) == 0x80:
                t = 1
                i += 2
            else:
                t = 0
                break
        elif (data[i] & 0x80) == 0x00:
            i += 1
            t = 1
        else:
            t = 0
            break
    if t == 1:
        return True
    else:
        return False

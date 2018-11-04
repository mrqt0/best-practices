#!/usr/bin/env python3

import re

string = "String %s, integer %02i, char %c"
raw_values = b"hello\x00\x00\x00\x00\x01\x00\x00\x00a"

r = re.compile("(%(?P<zero>0?)(?P<width>[0-9]*)(?P<type>[ifcs]))")
values = list()
offset = 0
for m in r.finditer(string):
    d = m.groupdict()
    t = d["type"]
    if t == "i":
        size = 4
        value = int.from_bytes(raw_values[:size], byteorder="big")
    elif t == "f":
        size = 8
        value = struct.unpack("d", raw_values[:size])
    elif t == "c":
        size = 4
        value = raw_values[:size].decode()[-1]
    elif t == "s":
        size = raw_values.find(b"\x00") + 1
        value = raw_values[:size - 1].decode()
    else:
        print("Unkown format specifier")
    values.append(value)
    raw_values = raw_values[size:]

# TODO: replace percent-style with python format strings
print(string % tuple(values))

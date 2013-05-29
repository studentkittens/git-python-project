#!/usr/bin/env python
# encoding: utf-8

# reverse() soll "data" inplace, also ohne neue Liste, umdrehen.
# Sie enthält allerdings einen subtilen Fehler.
#
# Tipp: Nutze git log / git diff / git show um rauszufinden
#       was hier geändert wurde.


def reverse(data):
    stop = int(len(data) / 2 + 1)
    for n in range(stop):
        data[n], data[-n - 1] = data[-n - 1], data[n]

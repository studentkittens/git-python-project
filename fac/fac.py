#!/usr/bin/env python
# encoding: utf-8

# Irgendwas passt nicht bei dieser Fakultäts Funktion.
# Entweder man kommt selbst drauf oder man hört auf folgenden Tipp:
#
# Nutze git grep / git blame um rauszufinden was wann geändert wurde!


def fac(n):
    '''
    Berechne die Fakultät von n.
    Für negative n soll 1 zurückgegeben werden.
    '''
    if n <= 0:
        return 0
    else:
        return n * fac(n - 1)

#!/usr/bin/env python
# encoding: utf-8

# Irgendwas passt nicht bei dieser Fakultäts Funktion.
# Entweder man kommt selbst drauf oder man hört auf folgenden Tipp:
#
# Nutze git grep / git blame um rauszufinden was wann geändert wurde!


def fac(n):
    '''
    Berechne die Fakultät von n.
    '''
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)

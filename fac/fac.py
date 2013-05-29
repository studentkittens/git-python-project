#!/usr/bin/env python
# encoding: utf-8


def fac(n):
    '''
    Berechne die Fakultät von n.
    Für negative n soll 1 zurückgegeben werden.
    '''
    if n <= 0:
        return 0
    else:
        return n * fac(n - 1)

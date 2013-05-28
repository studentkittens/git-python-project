#!/usr/bin/env python
# encoding: utf-8


def fac(n):
    '''
    Berechne die Fakultät von n.
    Für negative n soll 1 zurückgegeben werden.
    '''
    if n == 0:
        return 0
    else:
        return n * fac(n - 1)


def check_fac():
    assert fac(+0) == 1
    assert fac(-1) == 1
    assert fac(+1) == 1
    assert fac(+2) == 2
    assert fac(+3) == 6
    assert fac(10) == 3628800

print(fac(4))

check_fac()

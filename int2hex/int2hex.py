#!/usr/bin/env python
# encoding: utf-8


def int2hex(number):
    '''
    Soll aus einem Integer einen Hexstring machen. ("FF" == 255).
    Diese Methode ist nicht nur fürchterlich ineffzient, sondern auch falsch.

    Warum?

    Tipp: git blame / git grep könnten weiterhelfen.
    '''
    hexstring = '' if number > 0 else '0'

    while number > 0:
        hexstring += '0123456789ABCDEF'[number % 16]

        # Gehe eine Ziffer Weiter
        number = int(number / 10)

    return hexstring[::-1]

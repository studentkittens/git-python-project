#!/usr/bin/env python
# encoding: utf-8


def int2hex(number):
    '''
    Soll aus einem Integer einen Hexstring machen. (0xFF == 255).
    Diese Methode ist nicht nur fürchterlich ineffzient, sondern auch falsch.
    '''
    hexstring = '' if number > 0 else '0'

    while number > 0:
        hexstring += '0123456789ABCDEF'[number % 16]
        number = int(number / 16)

    return hexstring[::-1]

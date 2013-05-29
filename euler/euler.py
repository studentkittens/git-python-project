#!/usr/bin/env python
# encoding: utf-8


from functools import reduce


# Bei diesem Task enthält der Code keine offensichtlichen Fehler.
# Er ist aber viel zu langsam. Oh-oh.
#
# Man kann jetzt sich an die Numerik-Vorlesung erinnern,
# oder man schaut sich vlt. im repository um ob vlt. schon jemand
# sich die Arbeit gemacht hat?
#
# Viel Erfolg bei der Suche!
def fac(num):
    'Non-recursive fac() with reduce()'
    if num <= 0:
        return 1
    else:
        return reduce(lambda a, b: a * b, range(1, num + 1))


def euler(exp, num_iterations=200):
    y = 0
    for n in range(num_iterations):
        y += exp ** n / fac(n - 1)

    return y

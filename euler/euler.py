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


def euler(exp, num_iterations=100):
    y = 1.0
    fac = 1.0
    x_n = 1.0

    for n in range(1, num_iterations + 1):
        x_n *= exp
        fac *= n
        y += x_n / fac

    return y

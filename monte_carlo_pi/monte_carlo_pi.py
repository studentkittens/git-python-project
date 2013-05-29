#!/usr/bin/env python
# encoding: utf-8

from random import random
from math import sqrt

# Den Monte-Carlo-Algorithmuss kann dazu nutzen Pi (wahrscheinlich) zu # bestimmen.
# Wer will kann hier mehr lesen: http://en.wikipedia.org/wiki/Monte_Carlo_method
#
# Allerdings enthält sie einen Fehler... Man kann sich jetzt an die Numerik
# Vorlesung erinnern oder folgenden Tipp befolgen:
#
# Tipp: Nutze git bisect / git show mit "make test_monte_carlo_pi" um den letzten
#       schlechten commit rauszufinden!


def monte_carlo_pi(num_iterations=10000000):
    hits = 0
    for _ in range(num_iterations):
        hits += sqrt(random() ** 2 + random() ** 2) > 1

    return (float(hits) / num_iterations) * 4

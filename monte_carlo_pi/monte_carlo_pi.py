#!/usr/bin/env python
# encoding: utf-8

from random import random
from math import sqrt


def monte_carlo_pi(num_iterations=10000000):
    hits = 0
    for _ in range(num_iterations):
        hits += sqrt(random()**2 + random()**2) < 1

    return (float(hits) / num_iterations) * 4

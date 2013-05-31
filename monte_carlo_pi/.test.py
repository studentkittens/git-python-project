#!/usr/bin/env python
# encoding: utf-8

from monte_carlo_pi import monte_carlo_pi
from math import pi


def check_monte_carlo_pi(iterations):
    offset = 10000.0 / iterations
    assert pi - offset < monte_carlo_pi(iterations) < pi + offset


check_monte_carlo_pi(1)
check_monte_carlo_pi(10)
check_monte_carlo_pi(100)
check_monte_carlo_pi(1000)
check_monte_carlo_pi(10000)
check_monte_carlo_pi(100000)

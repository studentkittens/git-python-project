#!/usr/bin/env python
# encoding: utf-8

from euler import euler
from time import time
from math import e


def euler_timing(func, exp, times=200, iterations=200):
    diff = 0
    for n in range(times):
        start_time = time()
        func(exp, iterations)
        diff += time() - start_time
    return diff


def correct_euler(exp, num_iterations=200):
    y = 1
    fac = 1
    x_n = 1

    for n in range(1, num_iterations + 1):
        x_n *= exp
        fac *= n
        y += x_n / fac

    return y


# Berechne alle Werte von e^x von 0 bis 10
for x in range(20):
    correct = e ** x
    offset = correct / 10000000
    result = euler(x)



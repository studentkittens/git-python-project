#!/usr/bin/env python
# encoding: utf-8


def reverse(data):
    stop = int(len(data) / 2 + 1)

    for n in range(stop):
        data[n], data[-n - 1] = data[-n - 1], data[n]

#!/usr/bin/env python
# encoding: utf-8


def reverse_inplace(data):
    stop = int(len(data) / 2 + 1)

    print(stop)

    for n in range(stop):
        data[n], data[-n - 1] = data[-n - 1], data[n]

    print(data)


reverse_inplace([1,2,3,2,4,5])

#!/usr/bin/env python
# encoding: utf-8

from fibonacci import fibonacci


def check_fibonacci(results):
    'Returne True when die results die einer fibonacci liste entsprechen'
    if results[0] != 0 or results[1] != 1:
        return False

    for idx, num in enumerate(results[:-2]):
        if num + results[idx + 1] != results[idx + 2]:
            return False
    else:
        return True


assert check_fibonacci(fibonacci())

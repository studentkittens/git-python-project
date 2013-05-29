#!/usr/bin/env python
# encoding: utf-8

from int2hex import int2hex


assert int2hex(256) == '100'
assert int2hex(255) == 'FF'
assert int2hex(000) == '0'

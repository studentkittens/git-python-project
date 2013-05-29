#!/usr/bin/env python
# encoding: utf-8

from reverse import reverse
from copy import copy


def test_reverse(data):
    cdata = copy(data)
    reverse(cdata)
    assert cdata == data[::-1]


test_reverse([])
test_reverse([1,2,3])
test_reverse([1,2,3,4,5])
test_reverse([1,2,3,2,4,5])

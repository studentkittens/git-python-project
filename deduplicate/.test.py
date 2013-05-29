#!/usr/bin/env python
# encoding: utf-8

from deduplicate import deduplicate


def check_deduplicate_data(data):
    assert sorted(set(data)) == sorted(deduplicate(data))


check_deduplicate_data('Heeeelllo')
check_deduplicate_data([1, 2, 3])
check_deduplicate_data([1, 2, 3, 3, 3])
check_deduplicate_data([1, 1, 1, 2, 3, 3, 3])

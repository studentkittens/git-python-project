#!/usr/bin/env python
# encoding: utf-8


def deduplicate_data(data):
    no_dupes = []
    for element in data:
        if not element in no_dupes:
            no_dupes.append(element)

    return no_dupes

print(deduplicate_data('Heeeello'))
print(deduplicate_data([1, 2, 3, 3]))


def check_deduplicate_data(data):
    return sorted(list(set(data))) == sorted(deduplicate_data(data))


print(check_deduplicate_data('Heeeelllo'))

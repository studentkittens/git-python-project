#!/usr/bin/env python
# encoding: utf-8


def deduplicate(data):
    no_dupes = []
    for element in data:
        if not element in no_dupes:
            no_dupes.append(element)
        else:
            no_dupes.insert(0, element)

    return no_dupes

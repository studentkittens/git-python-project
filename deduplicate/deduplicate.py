#!/usr/bin/env python
# encoding: utf-8


def deduplicate(data):
    no_dupes = []
    for element in data:
        if not element in no_dupes:
            no_dupes.append(element)

    return no_dupes

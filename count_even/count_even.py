#!/usr/bin/env python
# encoding: utf-8

# Die count_event soll die Anzahl gerader Zahlen in einer Liste zählen.
# Allerdings enthält sie momentan einen Fehler. Wo?
#
# Wenn ihr wirklich nicht drauf kommt könnt ihr auch git log/diff/show nutzen
# um einen weiteren Tipp zu bekommen.


def count_even(iterable):
    count = 0
    for element in iterable:
        if element % 2 == 0:
            count += 1

    return count

#!/usr/bin/env python
# encoding: utf-8

# Bei dieser Funktion passt irgendwas nicht.
# Sie soll eine Liste "data" nehmen und diese
# von Duplikaten befreien.
# Die Reihenfolge soll dabei erhalten bleiben.

def deduplicate(data):
    no_dupes = []
    for element in data:
        if not element in no_dupes:
            no_dupes.append(element)

    return no_dupes

#!/usr/bin/env python
# encoding: utf-8


from random import shuffle


def scramble(sentence):
    words = []
    for word in sentence.split():
        shuffled = list(word[1:-1])
        shuffle(shuffled)
        words.append(word[0] + ''.join(shuffled) + word[-1])

    return ' '.join(words)

print(scramble("Katzen sind wirklich komische Tiere"))

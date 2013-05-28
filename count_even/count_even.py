def cound_event(iterable):
    count = 0
    for element in iterable:
        if element % 2 == 0:
            count += 1

    return count

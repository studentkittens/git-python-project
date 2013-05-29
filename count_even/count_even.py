def count_even(iterable):
    count = 0
    for element in iterable:
        if element % 2 == 1:
            count += 1

    return count

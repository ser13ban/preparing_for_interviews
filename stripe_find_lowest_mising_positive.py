from turtle import position


def lowest_min_positive(numbers: list):
    positives = set()
    maxim = -1
    for el in numbers:
        if el > maxim:
            maxim = el

        if el > 0 and el not in positives:
            positives.add(el)

    lowest = 1
    while lowest <= maxim:
        if lowest not in positives:
            return lowest
        lowest += 1

    return lowest


print(lowest_min_positive(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 9, 1, 2, 2, -1, -1]))

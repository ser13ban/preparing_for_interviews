# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def maxin_value(include: int, exclude: int):
    if include > exclude:
        return include
    else:
        return exclude


def non_adjacency_sum(numbers: list):
    include = numbers[0]
    exclude = 0

    for i in range(1, len(numbers)):
        new_exclude = maxin_value(include, exclude)

        include = exclude + numbers[i]
        exclude = new_exclude

    return maxin_value(include, exclude)


print(non_adjacency_sum([2, 4, 6, 2, 5]))
print(non_adjacency_sum([5, 1, 1, 5]))

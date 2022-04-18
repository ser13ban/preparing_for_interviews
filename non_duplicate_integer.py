# 1 2 3 1 2 3 1 2 3 4
from numpy import greater_equal
from pandas import pivot


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    smaller = []
    greater = []

    for number in numbers:
        if number < pivot:
            smaller.append(number)
        else:
            greater.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


def find_non_duplicate_integer(numbers):
    numbers = quick_sort(numbers)
    i = 0
    while i < len(numbers)-1:
        if numbers[i+1] != numbers[i]:
            return numbers[i]
        else:
            i += 3

    if numbers[len(numbers) - 1] != numbers[len(numbers) - 2]:
        return numbers[len(numbers)-1]


def find_non_duplicate_eficent(numbers):
    return (3 * sum(set(numbers)) - sum(numbers)) // 2


print(find_non_duplicate_eficent([1, 2, 3, 1, 2, 3, 1, 2, 3, 4]))
print(find_non_duplicate_integer([1, 2, 3, 1, 2, 3, 1, 2, 3, 4]))

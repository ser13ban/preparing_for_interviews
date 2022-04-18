from re import I


def multiples_of_3_and_5(n: int):
    sum = 0
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i

    print(sum)


def even_fib_numbers(n):
    s = 0
    counter = 2
    first = 0
    second = 1
    temp = 0
    while counter < n:
        counter += 1
        temp = first + second
        first = second
        second = temp
        if temp % 2 == 0:
            s += temp

    print(sum)


def evenFibSum(limit):
    if (limit < 2):
        return 0

    # Initialize first two even prime numbers
    # and their sum
    ef1 = 0
    ef2 = 2
    sm = ef1 + ef2

    # calculating sum of even Fibonacci value
    while (ef2 <= limit):

        # get next even value of Fibonacci
        # sequence
        ef3 = 4 * ef2 + ef1

        # If we go beyond limit, we break loop
        if (ef3 > limit):
            break

        # Move to next even number and update
        # sum
        ef1 = ef2
        ef2 = ef3
        sm = sm + ef2

        print(sum)


d = {}
d[(0, 1)] = 10
# print(d)


def reverse(x: int) -> int:
    negative = x < 0
    if negative:
        x = x * (-1)

    print(negative)

    s = str(x)
    s = s[::-1]
    print(s)
    try:
        x = int(s)

        if x > pow(2, 31-1) and not negative:
            return 0

        if negative and (x * -1) < pow(-2, 31):
            return 0

        if negative:
            return x*(-1)

        return x
    except:
        return 0


print(reverse(-2147483412))


def reverseArray(arr):
    # Write your code here
    i = 0
    j = len(arr)-1
    while i <= j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return arr


def maxIndex(steps, badIndex):
    # Write your code here
    maximum = 0
    for i in range(1, steps+1):
        maximum += i

    curr_i = maximum
    step = steps
    while True:
        while curr_i > 0 and steps > 0:
            curr_i -= steps
        if curr_i == badIndex:
            curr_i += steps

        steps -= 1

        if curr_i <= 0:
            return maximum

        steps = step
        curr_i = maximum - 1
        if curr_i == badIndex:
            curr_i = maximum - 1
            maximum -= 1


print(reverseArray([]))
x

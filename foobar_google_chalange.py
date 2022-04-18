import math
from cgitb import reset
from operator import length_hint


def solution(s):
    if not s:
        return 0

    nxt = [0]*len(s)
    for i in range(1, len(nxt)):
        k = nxt[i - 1]
        while True:
            if s[i] == s[k]:
                nxt[i] = k + 1
                break
            elif k == 0:
                nxt[i] = 0
                break
            else:
                k = nxt[k - 1]

    smallPieceLen = len(s) - nxt[-1]
    return len(s) // smallPieceLen


# print(solution("aabbbaabbbaabbb"))
def decoding(l, t):
    for i in range(len(l)):
        j = i+1
        current_sum = l[i]
        while j < len(l) and current_sum < t:
            current_sum += l[j]
            j += 1

        if current_sum == t:
            return [i, j-1]
    return [-1, -1]


#print(decoding([1, 2, 3, 4], 15))
#print(decoding([4, 3, 10, 2, 8], 12))

def salutes(s):
    right = 0
    result = 0
    for el in s:
        if el == ">":
            right += 1
        if el == "<":
            result += right
    return result*2


def xor(start, length):
    current = start-1
    skip = length+1
    result = start
    for i in range(length):
        skip -= 1
        for j in range(length):
            current += 1
            if current == start:
                continue
            if j < skip:
                result ^= current
    return result


#print(xor(0, 20000))
#print(xor(17, 4))


def Log2(x):
    return int(math.log10(x) / math.log10(2))


def closestMultiple(n, x):
    if x > n:
        return x
    z = (int)(x / 2)
    n = n + z
    n = n - (n % x)
    return n


def s(n):
    mutliple_of_2 = closestMultiple(n, 2)
    if mutliple_of_2 > n:
        return mutliple_of_2-n + math.log2(mutliple_of_2)
    elif mutliple_of_2 == n:
        return Log2(mutliple_of_2)
    else:
        return n-mutliple_of_2 + math.log2(mutliple_of_2)


print(s(4))

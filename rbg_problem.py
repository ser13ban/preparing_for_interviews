
def re_arange_rbg(s):
    i = 0
    j = len(s)-1
    # move the front of the list
    while True:
        while s[i] == 'R' and i < j:
            i += 1

        while s[j] != 'R' and i < j:
            j -= 1

        if i >= j:
            break

        aux = s[i]
        s[i] = s[j]
        s[j] = aux

    # move B to the left of the list:
    j = len(s) - 1
    while True:
        # find the first B
        while s[i] != 'B' and i < j:
            i += 1

        # find the last non B
        while s[j] == 'B' and i < j:
            j -= 1

        if i >= j:
            break

        aux = s[i]
        s[i] = s[j]
        s[j] = aux

    return s


print(re_arange_rbg(['G', 'B', 'R', 'R', 'B', 'R', 'G']))

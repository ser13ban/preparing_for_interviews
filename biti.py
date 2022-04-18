def max_subsequence(i, w, biti):
    j = i+(w-1)
    if j > len(biti)-1:
        j = len(biti)-1

    for index in range(j, i, -1):
        if biti[index] == "1":
            break
    return biti[i:index+1]


print(max_subsequence(0, 2, "111"))
print(max_subsequence(0, 5, "101101"))

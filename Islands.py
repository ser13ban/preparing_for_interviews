from collections import deque


def print_land(land):
    for i, row in enumerate(land):
        strr = ' '
        for j, val in enumerate(row):
            strr = strr + str(val) + ' '
        print(strr)


def are_indexes_in_bound(i, j, row_length, col_length):
    if i > 0 and i < row_length and j > 0 and j < col_length:
        return True

    return False


def length_of_river(i, j, land, row_len, col_len):
    stack = deque()
    stack.append((land[i][j], i, j))
    length = 1

    while len(stack) > 0:
        curent, i, j = stack.pop()

        if curent == 2:
            continue

        for add_row, add_col in [
            (+1, 0), (-1, 0), (0, +1), (0, -1)
        ]:
            index_i = i + add_row
            index_j = j + add_col
            if are_indexes_in_bound(index_i, index_j, row_len, col_len) and land[index_i][index_j] == 1:
                stack.append((land[index_i][index_j], index_i, index_j))
                land[index_i][index_j] = 2
                length += 1

        return length


def output_length_of_rivers(land):
    lengths = []
    count = 0
    for i, row in enumerate(land):
        for j, val in enumerate(row):
            if val == 1:
                river = length_of_river(i, j, land, len(row), len(row))
                lengths.append(river)
                count += 1

    return lengths, count


land = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
#
print(output_length_of_rivers(land))

#print( length_of_river(1,2,matrix,0) )

# Given a 2D array (n by n) of zeros and ones. (n>1)
# 1 means wall/concrete, and 0 means free space.
# Free spaces are only connected horizontally and vertically.
# The robot can only demolish at most one wall.
# The robot starts moving from one end of the room at (0,0). Find if the robot can reach the other end at (n-1, n-1) by demolishing at most 1 wall in the room.
# Write a function which will takes N and the 2D array as an argument, and return the boolean value true if the robot can go from (0,0) to (n-1,n-1), otherwise returns false.
# Grid (0,0) and grid(n-1,n-1) will always be free space, i.e., grid[0][0] = 0 and grid[n - 1][n - 1] = 0.
# Example 1

# Input 1:

# n = 6


# 0	0	1	1	0	0
# 0	0	1	1	0	0
# 0	0	1	1	0	0
# 0	0	1	1	0	0
# 0	0	1	1	0	0
# 0	0	1	1	0	0
# Output 1: false

# Example 2

# Input 2:

# n =6

# 0	0	1	1	0	0
# 0	0	1	1	0	0
# 0	0	0	1	0	0
# 0	0	1	1	0	1
# 0	0	1	1	0	0
# 0	0	1	1	0	0

# Output 2: true

# 0 is un used
# 1 is wall
# 2 visited
# 3 wass was broken
def are_indexes_in_bound(i, j, n):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    return True


def is_route_possible(initial_i, initial_j, board, n, demolished_before):
    curr_i = initial_i
    curr_j = initial_j
    if curr_i == n-1 and curr_j == n-1:
        return True

    for next_i, next_j in [(-1, 0), (+1, 0), (0, -1), (0, 1)]:
        curr_i += next_i
        curr_j += next_j
        if are_indexes_in_bound(curr_i, curr_j, n):
            if board[curr_i][curr_j] == 0:
                board[curr_i][curr_j] == 2
                is_route_possible(curr_i, curr_j, board, n, demolished_before)

            if board[curr_i][curr_j] == 1 and demolished_before == False:
                board[curr_i][curr_j] == 2
                is_route_possible(curr_i, curr_j, n, True)

            if board[curr_i][curr_j] == 1 and demolished_before == True:
                return False


A = [[0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]]
is_route_possible(0, 0, A, 6, False)

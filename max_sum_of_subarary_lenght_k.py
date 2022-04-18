from collections import deque


def find_maximum_sum_of_subarrays_len_k(arr, k):
    i = 1
    j = k+1
    result = []
    first_max = [-1, -1]
    second_max = [-1, -1]

    for index in range(i, j):
        if arr[i] > first_max[0]:
            second_max = first_max
            first_max[0] = arr[index]
            first_max[1] = index

        if arr[i] > second_max[0]:
            second_max[0] = arr[index]
            second_max[1] = index

    result.append(first_max[0])

    while j < len(arr):
        if first_max[1] == i-1:
            # in this case we will compare with the second max
            if arr[j] > second_max[0]:
                result.append(arr[j])
                first_max[0] = arr[j]
                first_max[1] = j
            else:
                first_max = second_max
                second_max[0] = arr[j]
                socond_max[1] = j

        else:
            # we will compare with the first_max
            if first_max[0] > arr[j]:
                result.append(arr[j])
                second_max[0] = arr[j]
                second_max[1] = j
        j += 1
        i += 1
    return result


def lengthLongestPath(input):
    stack = []
    current_level = 0
    res = 0
    for name in input.split('\n'):
        # print stack, current_level
        tabs = name.split('\t')
        if len(tabs) - 1 == current_level:
            if stack:
                stack.pop()
            stack.append(tabs[-1])
        elif len(tabs) - 1 > current_level:
            stack.append(tabs[-1])
        else:
            for _ in range(current_level - len(tabs) + 2):
                if stack:
                    stack.pop()
            stack.append(tabs[-1])
        if '.' in tabs[-1]:
            res = max(res, len('/'.join(stack)))
        current_level = len(tabs) - 1
    return res


def find_maximum_sum_of_subarrays_len_k(arr, k):
    result = []
    que = deque()
    for i in range(k):
        while que and arr[i] >= arr[que[-1]]:
            que.pop()
        que.append(i)

    for i in range(k, len(arr)):
        result.append(arr[que[0]])

        while que and que[0] <= i - k:
            que.popleft()

        while que and arr[i] >= arr[que[-1]]:
            que.pop()
        que.append(i)

    result.append(arr[que[0]])
    return result


arr = [10, 5, 2, 7, 8, 7]
n = len(arr)
print(find_maximum_sum_of_subarrays_len_k(arr, 3))

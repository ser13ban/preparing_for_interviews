def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    smaller = []
    greater = []

    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            smaller.append(item)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


def merge_sort(arr: list):
    if len(arr) > 1:
        left_slpit = arr[:len(arr)//2]
        right_slpit = arr[len(arr)//2:]
        merge_sort(left_slpit)
        merge_sort(right_slpit)
        i = 0
        j = 0
        k = 0
        while i < len(left_slpit) and j < len(right_slpit):
            if left_slpit[i] < right_slpit[j]:
                arr[k] = left_slpit[i]
                i += 1
            else:
                arr[k] = right_slpit[j]
                j += 1
            k += 1

        while i < len(left_slpit):
            arr[k] = left_slpit[i]
            i += 1
            k += 1

        while j < len(right_slpit):
            arr[k] = right_slpit[j]
            j += 1
            k += 1

    return arr


print(quick_sort([9, 8, 1, 5, 1, 0, 11, -9, 18, 2002, 18, 10]))
print(merge_sort([9, 8, 1, 5, 1, 0, 11, -9, 18, 2002, 18, 10]))

arr = [9, 8, 1, 5, 1, 0, 11, -9, 18, 2002, 18, 10]
print(arr[1:2])

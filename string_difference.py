from black import diff


def find_edit_difference(str1, str2):
    len_string1 = len(str1)
    len_string2 = len(str2)
    if len_string1 > len(str2):
        difference = len_string1 - len_string2
        print(str1)
        # str1[:difference]

    elif len_string1 < len_string2:
        difference = len_string2 - len_string1
        # str2[:difference]

    else:
        difference = 0

    for i in range(len_string1):
        if str1[i] != str2[i]:
            difference += 1
    return difference


print(find_edit_difference("kitten", "sitttttinghhh"))

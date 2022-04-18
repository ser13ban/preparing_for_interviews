def getFather(node):
    # counts the number of \t in the node
    return node.count("\t") - 1


def construct_tree(files):
    i = 0
    tree = {}
    nodes = files.split("\n")
    for node in nodes:
        father = getFather(node)
        if tree.keys().index(father):
            tree[tree.keys().index(father)].append(node)
        else:
            tree[node] = []
    return tree


def print_dict(dic):
    for key, values in dic.items():
        print(f"node: {key} with children: {values}")


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


files = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(lengthLongestPath(files))

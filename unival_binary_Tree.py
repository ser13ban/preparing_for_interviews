class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isUnivalTree(root, count: int):
    if root == None:
        count += 1
        return [True, count]

    isUniVal = True
    if root.left:
        isUniVal = isUnivalTree(
            root.left, count)[0] and isUniVal and root.left.val == root.val

    if root.right:
        isUniVal = isUnivalTree(
            root.right, count)[0] and isUniVal and root.right.val == root.val

    if not isUniVal:
        return [False, count]
    count += 1
    return [True, count]


def test_1():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(4)
    root.right.right = Node(5)
    return isUnivalTree(root, 1)


print(test_1())

from collections import deque


def getPowerset(s):
    result = []

    def findPowerSet(originalSet, generatedSet, n):
        if n == 0:
            print(generatedSet)
            result.append(list(generatedSet))
            return

        generatedSet.appendleft(originalSet[n-1])
        findPowerSet(originalSet, generatedSet, n-1)

        generatedSet.popleft()
        findPowerSet(originalSet, generatedSet, n-1)

    current = deque()
    findPowerSet(s, current, len(s))
    return result


print(getPowerset([1, 2]))

from collections import deque


stack = deque()

for i in range(10):
    stack.append(i)
print(stack)
stack.pop()
stack.pop()
stack.pop()
stack.append(10)
print(stack)

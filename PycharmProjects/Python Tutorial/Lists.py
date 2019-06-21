from collections import deque

queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())
print(queue.popleft())

print(queue)

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

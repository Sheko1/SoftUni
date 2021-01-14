from collections import deque

food = int(input())

orders = [int(order) for order in input().split()]

queue = deque(orders)
print(max(queue))

while queue:
    order = queue[0]

    if order <= food:
        food -= order
        queue.popleft()

    else:
        print(f"Orders left: {' '.join(map(str, queue))}")
        break

if not queue:
    print("Orders complete")
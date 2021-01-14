from collections import deque

n = int(input())

stations = []

for _ in range(n):
    stations.append(input())

que = deque(stations)
stations_1 = stations.copy()
index = 0
while que:
    tank = 0
    index = stations.index(que[0])
    for _ in range(n):
        petrol, distance = que.popleft().split()

        tank += int(petrol)
        if tank >= int(distance):
            tank -= int(distance)

        else:
            que = deque(stations_1)
            que.append(que.popleft())
            stations_1 = list(que)
            break

print(index)
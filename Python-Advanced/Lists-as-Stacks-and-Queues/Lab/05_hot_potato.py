from collections import deque

players = deque()
[players.append(name) for name in input().split()]

turns = int(input())

while len(players) > 1:
    players.rotate(-turns + 1)
    print(f"Removed {players.popleft()}")

print(f"Last is {players.popleft()}")
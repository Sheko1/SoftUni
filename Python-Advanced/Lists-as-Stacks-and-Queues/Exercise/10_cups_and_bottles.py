from collections import deque

cups = deque(int(cup) for cup in input().split())
bottles = [int(bottle) for bottle in input().split()]

wasted_watter = 0
is_filled = False
while cups and bottles:
    bottle = bottles.pop()
    cup = cups[0]

    if bottle - cup >= 0:
        cups.popleft()
        wasted_watter += (bottle - cup)

    else:
        cups[0] -= bottle

if not cups:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")

else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_watter}")
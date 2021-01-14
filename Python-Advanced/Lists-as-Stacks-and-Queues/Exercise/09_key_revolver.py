from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque(int(lock) for lock in input().split())
money = int(input())

bullets_cost = 0
reload_time = gun_barrel

while bullets and locks:
    bullet = bullets.pop()
    reload_time -= 1
    bullets_cost += bullet_price

    if bullet <= locks[0]:
        print("Bang!")
        locks.popleft()

    else:
        print("Ping!")

    if reload_time == 0 and bullets:
        reload_time = gun_barrel
        print("Reloading!")


if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money - bullets_cost}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
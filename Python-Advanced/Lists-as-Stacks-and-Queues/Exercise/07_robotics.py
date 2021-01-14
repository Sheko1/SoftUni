from collections import deque
from datetime import datetime, timedelta

robots = input().split(";")
clock = datetime.strptime(input(), "%H:%M:%S")
product = input()

product_que = deque()
available_robots = deque(robots)
robots_process_time = {}

while product != "End":
    product_que.append(product)
    product = input()


while product_que:
    clock = clock + timedelta(seconds=1)

    if available_robots:
        name, process_time = available_robots.popleft().split("-")

        robots_process_time[name] = clock + timedelta(seconds=int(process_time))

        print(f"{name} - {product_que.popleft()} [{clock.time()}]")

    else:
        for key in robots_process_time:
            if clock >= robots_process_time[key]:
                [available_robots.append(name) for name in robots if name.startswith(key)]

        if not available_robots:
            product_que.append(product_que.popleft())\

        else:
            name, process_time = available_robots.popleft().split("-")

            robots_process_time[name] = clock + timedelta(seconds=int(process_time))

            print(f"{name} - {product_que.popleft()} [{clock.time()}]")

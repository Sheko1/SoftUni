from collections import deque

green_light_range = int(input())
free_window = int(input())

command = input()
passed_cars = 0
cars = deque()
crash = False


while command != "END":
    if command == "green" and cars:
        time = green_light_range
        while time > 0 and cars:
            car = cars.popleft()

            if time - len(car) < 0:
                time_left = len(car) - time
                if free_window - time_left < 0:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[-(time_left - free_window)]}.")
                    crash = True
                    break

                else:
                    passed_cars += 1
                    time = 0

            else:
                passed_cars += 1
                time -= len(car)

    else:
        cars.append(command)

    if crash:
        break
    command = input()
if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
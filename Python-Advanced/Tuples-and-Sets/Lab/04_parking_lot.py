def input_lines(times):
    lines = []
    for _ in range(times):
        lines.append(input())

    return lines


def print_result(elements):
    if elements:
        for el in elements:
            print(el)

    else:
        print("Parking Lot is Empty")


n = int(input())
cars_data = input_lines(n)

parking_lots = set()

for car in cars_data:
    command, car_number = car.split(", ")
    if command == "IN":
        parking_lots.add(car_number)

    else:
        parking_lots.remove(car_number)

print_result(parking_lots)

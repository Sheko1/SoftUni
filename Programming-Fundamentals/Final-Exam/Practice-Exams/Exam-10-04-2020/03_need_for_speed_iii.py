n_cars = int(input())

cars = {}

for _ in range(n_cars):
    car = input().split("|")

    if car[0] not in cars:
        cars[car[0]] = {}
        cars[car[0]]['mileage'] = int(car[1])
        cars[car[0]]['fuel'] = int(car[2])

command = input()

while command != "Stop":
    data = command.split(" : ")

    if data[0] == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])

        if fuel > cars[car]['fuel']:
            print("Not enough fuel to make that ride")

        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]['mileage'] > 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")

    elif data[0] == "Refuel":
        car = data[1]
        fuel = int(data[2])

        if fuel + cars[car]['fuel'] > 75:
            fuel = 75 - cars[car]['fuel']

        cars[car]['fuel'] += fuel

        print(f"{car} refueled with {fuel} liters")

    elif data[0] == "Revert":
        car = data[1]
        km = int(data[2])

        if cars[car]['mileage'] - km < 10000:
            cars[car]['mileage'] = 10000

        else:
            cars[car]['mileage'] -= km
            print(f"{car} mileage decreased by {km} kilometers")

    command = input()

cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))
[print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.") for key, value in cars]

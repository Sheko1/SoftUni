n = int(input())
plants = {}

for _ in range(n):
    plant = input().split("<->")
    plants[plant[0]] = {'rarity': int(plant[1]), 'rate': []}

command = input()

while command != "Exhibition":
    data = command.split(maxsplit=1)

    if data[0] == "Rate:":
        plant, rating = data[1].split(" - ")

        if plant in plants:
            plants[plant]['rate'].append(int(rating))

        else:
            print("error")

    elif data[0] == "Update:":
        plant, new_rarity = data[1].split(" - ")

        if plant in plants:
            plants[plant]['rarity'] = int(new_rarity)

        else:
            print("error")

    elif data[0] == "Reset:":
        plant = data[1]

        if plant in plants:
            plants[plant]['rate'] = []

        else:
            print("error")

    command = input()

for key in plants:
    if len(plants[key]['rate']) > 0:
        plants[key]['rate'] = sum(plants[key]['rate']) / len(plants[key]['rate'])

    else:
        plants[key]['rate'] = 0

plants = sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rate']))

print("Plants for the exhibition:")
[print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rate']:.2f}") for key, value in plants]
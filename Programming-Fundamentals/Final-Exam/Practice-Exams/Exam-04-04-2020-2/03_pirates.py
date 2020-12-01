command = input()
towns = {}
while command != "Sail":
    data = command.split("||")
    if data[0] not in towns:
        towns[data[0]] = {}
        towns[data[0]]['population'] = int(data[1])
        towns[data[0]]['gold'] = int(data[2])

    else:
        towns[data[0]]['population'] += int(data[1])
        towns[data[0]]['gold'] += int(data[2])

    command = input()

event = input()

while event != "End":
    data = event.split("=>", maxsplit=1)

    if data[0] == "Plunder":
        town, people, gold = data[1].split("=>")
        people = int(people)
        gold = int(gold)

        towns[town]['population'] -= people
        towns[town]['gold'] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if towns[town]['population'] <= 0 or towns[town]['gold'] <= 0:
            towns.pop(town)

            print(f"{town} has been wiped off the map!")

    elif data[0] == "Prosper":
        town, gold = data[1].split("=>")
        gold = int(gold)

        if gold < 0:
            print("Gold added cannot be a negative number!")

        else:
            towns[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")

    event = input()

towns = sorted(towns.items(), key=lambda x: (-x[1]['gold'], x[0]))

print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")

for town in towns:
    print(f"{town[0]} -> Population: {town[1]['population']} citizens, Gold: {town[1]['gold']} kg")

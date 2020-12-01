n = int(input())

heroes = {}

for _ in range(n):
    hero = input().split()

    if hero[0] not in heroes:
        if int(hero[1]) <= 100 and int(hero[-1]) <= 200:
            heroes[hero[0]] = {}
            heroes[hero[0]]['HP'] = int(hero[1])
            heroes[hero[0]]['MP'] = int(hero[-1])


command = input()

while command != "End":
    data = command.split(" - ")

    if data[0] == "CastSpell":
        name = data[1]
        mp = int(data[2])
        spell = data[3]

        if mp > heroes[name]['MP']:
            print(f"{name} does not have enough MP to cast {spell}!")

        else:
            heroes[name]['MP'] -= mp
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['MP']} MP!")

    elif data[0] == "TakeDamage":
        name = data[1]
        dmg = int(data[2])
        attacker = data[3]

        heroes[name]['HP'] -= dmg

        if heroes[name]['HP'] <= 0:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")

        else:
            print(f"{name} was hit for {dmg} HP by {attacker} and now has {heroes[name]['HP']} HP left!")

    elif data[0] == "Recharge":
        name = data[1]
        amount = int(data[2])

        if amount + heroes[name]['MP'] > 200:
            amount = 200 - heroes[name]['MP']

        heroes[name]['MP'] += amount

        print(f"{name} recharged for {amount} MP!")

    elif data[0] == "Heal":
        name = data[1]
        amount = int(data[2])

        if amount + heroes[name]['HP'] > 100:
            amount = 100 - heroes[name]['HP']

        heroes[name]['HP'] += amount

        print(f"{name} healed for {amount} HP!")

    command = input()

heroes = sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0]))
[print(f"{key}\nHP: {value['HP']}\nMP: {value['MP']}") for key, value in heroes]

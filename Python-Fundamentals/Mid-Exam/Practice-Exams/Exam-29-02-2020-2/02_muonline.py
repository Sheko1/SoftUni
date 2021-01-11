rooms = input().split("|")

health = 100
bitcoins = 0
best_room = 0
is_dead = False

for i in range(len(rooms)):
    data = rooms[i].split()

    if data[0] == "potion":
        heal = int(data[1])
        if health + heal > 100:
            heal = 100 - health
            health += heal

        else:
            health += int(data[1])

        print(f"You healed for {heal} hp.")
        print(f"Current health: {health} hp.")

    elif data[0] == "chest":
        bitcoins += int(data[1])
        print(f"You found {int(data[1])} bitcoins.")

    else:
        health -= int(data[1])
        if health <= 0:
            print(f"You died! Killed by {data[0]}.")
            best_room = i+1
            is_dead = True
            break

        else:
            print(f"You slayed {data[0]}.")

if is_dead:
    print(f"Best room: {best_room}")

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

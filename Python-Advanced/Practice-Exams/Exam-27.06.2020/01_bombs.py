from collections import deque


def bomb_filler_and_is_full_check(bomb_to_fill, variable, bombs):
    bombs[bomb_to_fill] += 1

    if bombs[bomb_to_fill] == 3:
        variable.append(1)

    return bombs, variable


def print_list_or_empty(the_list, name):
    if the_list:
        print(f"{name}: {', '.join(str(x) for x in the_list)}")

    else:
        print(f"{name}: empty")


BOMB_TYPES = {"datura": 40, "cherry": 60, "smoke": 120}

bomb_effect = deque([int(num) for num in input().split(", ")])
bomb_casing = [int(num) for num in input().split(", ")]

created_bombs = {"Cherry Bombs:": 0, "Datura Bombs:": 0, "Smoke Decoy Bombs:": 0}
is_filled = []

while bomb_casing and bomb_effect:
    if len(is_filled) == 3:
        break

    curr_bomb_effect = bomb_effect[0]
    curr_bomb_casing = bomb_casing[-1]

    bomb = curr_bomb_casing + curr_bomb_effect

    if bomb == BOMB_TYPES["datura"]:
        created_bombs, is_filled = bomb_filler_and_is_full_check("Datura Bombs:", is_filled, created_bombs)

    elif bomb == BOMB_TYPES['cherry']:
        created_bombs, is_filled = bomb_filler_and_is_full_check("Cherry Bombs:", is_filled, created_bombs)

    elif bomb == BOMB_TYPES["smoke"]:
        created_bombs, is_filled = bomb_filler_and_is_full_check("Smoke Decoy Bombs:", is_filled, created_bombs)

    else:
        bomb_casing[-1] -= 5
        continue

    bomb_effect.popleft()
    bomb_casing.pop()


if len(is_filled) == 3:
    print("Bene! You have successfully filled the bomb pouch!")

else:
    print("You don't have enough materials to fill the bomb pouch.")


print_list_or_empty(bomb_effect, "Bomb Effects")
print_list_or_empty(bomb_casing, "Bomb Casings")

[print(f"{key} {value}") for key, value in created_bombs.items()]

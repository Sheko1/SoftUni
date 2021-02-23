from collections import deque


def is_enough_fireworks(fireworks_dict):
    if fireworks_dict["Palm Fireworks"] >= 3 and fireworks_dict["Willow Fireworks"] >= 3\
            and fireworks_dict["Crossette Fireworks"] >= 3:
        return True

    return False


def get_int_list():
    return [int(x) for x in input().split(", ")]


def remove_effect_and_power(effect_list, power_list):
    effect_list.popleft()
    power_list.pop()


def print_fireworks(the_dict):
    for key, value in the_dict.items():
        print(f"{key}: {value}")


firework_effects = deque(get_int_list())
explosive_powers = get_int_list()
fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while firework_effects and explosive_powers:
    current_effect = firework_effects[0]
    current_power = explosive_powers[-1]
    the_mix = current_effect + current_power

    if current_effect <= 0:
        firework_effects.popleft()
        continue

    elif current_power <= 0:
        explosive_powers.pop()
        continue

    if is_enough_fireworks(fireworks):
        break

    if the_mix % 3 == 0 and the_mix % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        remove_effect_and_power(firework_effects, explosive_powers)

    elif the_mix % 5 == 0 and the_mix % 3 != 0:
        fireworks["Willow Fireworks"] += 1
        remove_effect_and_power(firework_effects, explosive_powers)

    elif the_mix % 3 == 0 and the_mix % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
        remove_effect_and_power(firework_effects, explosive_powers)

    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.popleft())


if is_enough_fireworks(fireworks):
    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can’t make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print_fireworks(fireworks)

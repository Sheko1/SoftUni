def input_guests(times):
    lines = []
    for _ in range(times):
        lines.append(input())

    return lines


def print_result(elements):
    elements = sorted(elements)
    print(len(elements))
    for el in elements:
        print(el)


def input_arrived_guests():
    arrived = []
    guest_input = input()
    while guest_input != "END":
        arrived.append(guest_input)
        guest_input = input()

    return arrived


n = int(input())
guests = input_guests(n)

arrived_guests = input_arrived_guests()

guests = set(guests)
for guest in arrived_guests:
    guests.remove(guest)

print_result(guests)
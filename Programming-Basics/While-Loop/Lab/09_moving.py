width = int(input())
length = int(input())
height = int(input())
command = input()

space = width * length * height
boxes = 0

while command != "Done":
    box = int(command)
    boxes += box

    if boxes > space:
        break

    command = input()

if boxes > space:
    needed = boxes - space
    print(f"No more free space! You need {needed} Cubic meters more.")

else:
    more = space - boxes
    print(f"{more} Cubic meters left.")

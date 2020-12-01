people = int(input())
elevator = int(input())

courses = 0
while people > 0:
    if people > elevator:
        people -= elevator
        courses += 1
    else:
        people -= people
        courses += 1

print(courses)

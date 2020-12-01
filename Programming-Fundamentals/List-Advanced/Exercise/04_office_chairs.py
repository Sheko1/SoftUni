n = int(input())

chairs_count = 0

for i in range(1, n+1):
    chairs = input().split()
    if len(chairs[0]) > int(chairs[1]):
        chairs_count += len(chairs[0]) - int(chairs[1])

    elif len(chairs[0]) < int(chairs[1]):
        needed_chairs = int(chairs[1]) - len(chairs[0])
        print(f"{needed_chairs} more chairs needed in room {i}")
        chairs_count -= needed_chairs

if chairs_count >= 0:
    print(f"Game On, {chairs_count} free chairs left")
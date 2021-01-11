from collections import deque

que = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(que)} people remaining.")
        break

    elif command == "Paid":
        while que:
            print(que.popleft())

    else:
        que.append(command)
rows = int(input())

maze = []

for _ in range(rows):
    maze.append(input())

is_not_out = False
is_out = False

index = 0

while index in range(len(maze)):
    if "k" in maze[index]:
        maze[index] = maze[index].replace(" ", "k")

        if index == len(maze)-1:
            is_out = True
            break

        for i in range(len(maze[index])):
            if maze[index][i] == "k":
                if i == len(maze[index])-1 or i == 0:
                    is_out = True
                    break

                elif index+1 in range(len(maze)) and maze[index+1][i] == " ":
                    maze[index+1] = maze[index+1][:i] + "k" + maze[index+1][i+1:]
                    index += 1
                    break

            if i == len(maze[index])-1:
                is_not_out = True
                break

    else:
        index += 1

    if is_out:
        break

    elif is_not_out:
        break

if is_out:
    count = "".join(maze)
    print(f"Kate got out in {count.count('k')} moves")

else:
    print("Kate cannot get out")
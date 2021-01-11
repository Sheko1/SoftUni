string = input()
result = string
queue = 0
for i in range(len(string)):
    if string[i].isdigit() and string[i-1] == ">":
        value = int(string[i]) + queue
        remove = string[i:i+value]

        if ">" in remove:
            remove_1 = ""
            for index in range(len(remove)):
                if remove[index] == ">":
                    break

                elif remove[index].isdigit():
                    queue += int(remove[index])

                queue -= 1
                remove_1 += remove[index]

            remove = remove_1

        else:
            queue = 0

        result = result.replace(remove, "", 1)

print(result)
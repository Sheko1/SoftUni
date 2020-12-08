command = input()

players = {}

while command != "Season end":
    if len(command.split(" -> ")) > 1:
        data = command.split(" -> ")

        if data[0] not in players:
            players[data[0]] = {data[1]: int(data[2])}

        else:
            if data[1] in players[data[0]]:
                if int(data[2]) > players[data[0]][data[1]]:
                    players[data[0]][data[1]] = int(data[2])

            else:
                players[data[0]][data[1]] = int(data[2])
    else:
        data = command.split(" vs ")

        if data[0] in players and data[1] in players:
            position = ""

            for key in players[data[0]]:
                for k in players[data[1]]:
                    if key == k:
                        position = key

            if position:
                if players[data[0]][position] > players[data[1]][position]:
                    players.pop(data[1])

                elif players[data[1]][position] > players[data[0]][position]:
                    players.pop(data[0])

    command = input()

players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x))

for key, value in players:
    print(f"{key}: {sum(value.values())} skill")
    value = sorted(value.items(), key=lambda x: (-x[1], x))
    [print(f"- {position} <::> {skill}") for position, skill in value]

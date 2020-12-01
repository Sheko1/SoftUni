cards = input()

data = cards.split()
team_a = 11
team_b = 11
same_players = []
is_terminated = False

for i in range(len(data)):
    if "A" in data[i]:
        same_players.append(data[i])
        count = 0
        for j in range(len(same_players)):
            if data[i] == same_players[j]:
                count += 1

        if count <= 1:
            team_a -= 1

    if "B" in data[i]:
        same_players.append(data[i])
        count = 0
        for j in range(len(same_players)):
            if data[i] == same_players[j]:
                count += 1

        if count <= 1:
            team_b -= 1

    if team_a < 7 or team_b < 7:
        is_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if is_terminated:
    print("Game was terminated")

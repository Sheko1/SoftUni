n = int(input())

songs = {}

for _ in range(n):
    data = input().split("|")
    songs[data[0]] = {'composer': data[1], 'key': data[2]}

command = input()

while command != "Stop":
    data = command.split("|")

    if data[0] == "Add":
        piece = data[1]
        composer = data[2]
        key = data[3]

        if piece not in songs:
            songs[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    elif data[0] == "Remove":
        piece = data[1]

        if piece in songs:
            songs.pop(piece)
            print(f"Successfully removed {piece}!")

        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif data[0] == "ChangeKey":
        piece = data[1]
        key = data[2]

        if piece in songs:
            songs[piece]['key'] = key
            print(f"Changed the key of {piece} to {key}!")

        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

songs = sorted(songs.items(), key=lambda x: (x, x[1]['composer']))
[print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}") for key, value in songs]

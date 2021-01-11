command = input()

participants = {}
submissions = {}

while command != "exam finished":
    if "banned" not in command:
        username, language, points = command.split("-")
        points = int(points)

        if username not in participants:
            participants[username] = points

        else:
            if participants[username] < points:
                participants[username] = points

        if language not in submissions:
            submissions[language] = 1

        else:
            submissions[language] += 1

    elif "banned" in command:
        username = command.split("-", maxsplit=1)[0]

        participants.pop(username)

    command = input()

participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
submissions = sorted(submissions.items(), key=lambda x: (-x[1], x[0]))

print("Results:")
[print(f"{participant} | {score}") for participant, score in participants]
print("Submissions:")
[print(f"{language} - {submission}") for language, submission in submissions]
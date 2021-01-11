contest = input()
data = {}
users = {}

while contest != "end of contests":
    contest_data = contest.split(":")
    data[contest_data[0]] = contest_data[1]

    contest = input()

command = input()

while command != "end of submissions":
    submission_data = command.split("=>")

    if submission_data[0] in data:
        if submission_data[1] == data[submission_data[0]]:
            if submission_data[2] not in users:
                users[submission_data[2]] = {}

            if submission_data[0] not in users[submission_data[2]]:
                users[submission_data[2]][submission_data[0]] = int(submission_data[3])

            else:
                if int(submission_data[3]) > users[submission_data[2]][submission_data[0]]:
                    users[submission_data[2]][submission_data[0]] = int(submission_data[3])

    command = input()

max_points = [(key, sum(value.values())) for key, value in users.items()
              if max(sum(v.values()) for k, v in users.items()) == sum(value.values())]

users = sorted(users.items(), key=lambda x: x)

print(f"Best candidate is {max_points[0][0]} with total {max_points[0][1]} points.")
print("Ranking:")
for key, value in users:
    value = dict(sorted(value.items(), key=lambda x: -x[1]))
    print(key)
    [print(f"#  {key} -> {value}") for key, value in value.items()]
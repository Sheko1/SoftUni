import re

n = int(input())
pattern = r"U\$(?P<user>[A-Z][a-z]{2,})U\$P@\$(?P<pass>[A-Za-z]{5,}\d+)P@\$"
successful_registrations = 0

for register in range(n):
    data = input()
    match = re.match(pattern, data)

    if match:
        match = match.groupdict()
        successful_registrations += 1

        print("Registration was successful")
        print(f"Username: {match['user']}, Password: {match['pass']}")

    else:
        print("Invalid username or password")

print(f"Successful registrations: {successful_registrations}")
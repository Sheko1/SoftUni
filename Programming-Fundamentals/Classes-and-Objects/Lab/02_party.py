class Party:
    def __init__(self):
        self.people = []

    def add_people(self, name):
        self.people.append(name)


command = input()

party = Party()

while command != "End":
    party.add_people(command)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

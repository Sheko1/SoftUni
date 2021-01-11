import re

places = input()

patter = r"([=/])\b(?P<des>[A-Z][a-zA-Z]{2,})\b\1"
valid_places = re.finditer(patter, places)

travel_points = 0
destinations = []

for valid_place in valid_places:
    obj = valid_place.groupdict()

    destinations.append(obj['des'])
    travel_points += len(obj['des'])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
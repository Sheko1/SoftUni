key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
last_key = ""

while key_materials['shards'] < 250 and key_materials['fragments'] < 250 and key_materials['motes'] < 250:
    materials = [el.lower() for el in input().split()]

    for index in range(0, len(materials), 2):
        value = int(materials[index])
        key = materials[index+1]
        last_key = key

        if key in key_materials:
            key_materials[key] += value

            if key_materials[key] >= 250:
                break

        else:
            if key not in junk_materials:
                junk_materials[key] = value

            else:
                junk_materials[key] += value

key_materials[last_key] -= 250

if last_key == "shards":
    print("Shadowmourne obtained!")

elif last_key == "fragments":
    print("Valanyr obtained!")

elif last_key == "motes":
    print("Dragonwrath obtained!")

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))

[print(f"{key}: {value}") for key, value in key_materials.items()]
[print(f"{key}: {value}") for key, value in junk_materials.items()]
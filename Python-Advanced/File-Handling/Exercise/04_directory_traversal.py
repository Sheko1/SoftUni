import os

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
path = input()

files = os.listdir(path)
files = [el for el in files if os.path.isfile(el)]
result = {}

for file in files:
    file_name, extension = os.path.splitext(file)

    if extension not in result:
        result[extension] = []

    result[extension].append(file)

result = sorted(result.items(), key=lambda x: x)

with open(f"{desktop}/report.txt", "w") as file:
    for el in result:
        file.write(el[0]+"\n")

        for f in sorted(el[1], key=lambda x: x.lower()):
            file.write(f"- - - {f}\n")

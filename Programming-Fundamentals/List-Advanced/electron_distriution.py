electrons = int(input())
data = []
merfin = 0
while electrons > 0:
    merfin += 1
    formule = 2*merfin ** 2

    if electrons - formule < 0:
        formule = electrons

    electrons -= formule
    data.append(formule)

print(data)
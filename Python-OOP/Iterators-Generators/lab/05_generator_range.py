def genrange(start, end):
    return (x for x in range(start, end+1))


for i in genrange(1, 10):
    print(i)

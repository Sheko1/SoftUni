def solution():
    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        n = integers()
        while True:
            yield next(n) / 2

    def take(n, seq):
        result = []
        counter = 0
        for num in seq:
            if counter == n:
                break
            result.append(num)
            counter += 1

        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

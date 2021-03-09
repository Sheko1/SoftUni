import random


class RandomList(list):
    def get_random_element(self):
        el = random.choice(self)
        self.remove(el)
        return el


test = RandomList(["kahraman", "merfin", "tekin", "osman"])

while test:
    print(test)
    print(test.get_random_element())

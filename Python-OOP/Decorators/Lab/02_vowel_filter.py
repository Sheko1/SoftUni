import functools


def vowel_filter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        vowels = set("aeiou").union("aeiou".upper())
        result = func(*args, **kwargs)
        return [el for el in result if el in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

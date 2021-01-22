country = input().split(", ")
capital = input().split(", ")

pairs = zip(country, capital)
pairs = tuple(pairs)

# result = {country: capital for country, capital in pairs}
# [print(f"{country} -> {capital}") for country, capital in result.items()]
[print(f"{country} -> {capital}") for country, capital in pairs]

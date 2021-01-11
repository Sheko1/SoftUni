days = int(input())
food = float(input())

dog_eat = 0
cat_eat = 0
biscuits = 0
total = 0

for i in range(1, days+1):
    dog_food = int(input())
    cat_food = int(input())

    dog_eat += dog_food
    cat_eat += cat_food
    total = dog_eat + cat_eat

    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total/food*100:.2f}% of the food has been eaten.')
print(f'{dog_eat/total*100:.2f}% eaten from the dog.')
print(f'{cat_eat/total*100:.2f}% eaten from the cat.')

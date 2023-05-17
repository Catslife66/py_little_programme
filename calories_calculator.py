food_dict = {
    'avocado': 208, 'cheese': 371, 'fish': 1147, 'apple': 49, 'carrot': 33,
    'lemon': 31, 'chicken': 165, 'egg': 157, 'rice': 323, 'bread': 239,
}
ate_today = []
count = 0
limit = 1500

while True:
    food = input('What did you have to eat? ')
    if food == 'done':
        break
    else:
        ate_today.append(food)

for item in ate_today:
    count += food_dict[item]

if count > limit:
    print(f"You have eaten over {count-limit} calorie.")
elif count == limit:
    print("You have reached your calorie limit today.")
else:
    print(f"You can still eat {limit-count} calorie of food.")

print(f"Your calorie of food is {count}.")

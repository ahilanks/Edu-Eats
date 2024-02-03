import random

print('Welcome to EduEats!')
location = input('Which location are you planning to eat on for this week?\n')
calorie = input('What is your calorie goal?\n')
under_over = input('Are you trying to be under or over that goal?\n')



if location.lower() == 'cafe 3':
    range_start = 0
elif location.lower() == 'clark kerr':
    range_start = 3
elif location.lower() == 'crossroads':
    range_start = 6
elif location.lower() == 'foothill':
    range_start = 9

for i in range(5):
    breakfast_menu = random.choice(loc[range_start])
    lunch_menu = random.choice(loc[range_start+1])
    dinner_menu = random.choice(loc[range_start+2])

print('Breakfast Menu: ', breakfast_menu)
print()
print('Lunch Menu: ', lunch_menu)
print()
print('Dinner Menu: ', dinner_menu)
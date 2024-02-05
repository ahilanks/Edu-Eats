import datetime
import json
from geopy.geocoders import Nominatim
from geopy.point import Point
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

response = urlopen(url)
data = json.load(response)

print(data)

#crossroads: (37.866984,-122.256181)
#cafe 3: (37.867299,-122.260466)
#foothill: (37.875342,-122.256148)
# clark kher: (37.863745,-122.249851)




print('Welcome to EduEats!')
location = input('Which location are you planning to eat on for this week?\n')
print()
print('Dietary Preferences:')
vegan = input("Are you vegan?[Y/N]\n")
if vegan == 'N':
    vegetarian = input("Are you vegetarian?[Y/N]\n")
else: vegetarian = 'N'
# halal = input("Only Halal?[Y/N]\n")
# kosher = input("Only Kosher?[Y/N]\n")
print() 
print('Allergies:')
# gluten = input("Gluten?[Y/N]\n")
milk = input("Milk?[Y/N]\n")
# Egg = input("Egg?[Y/N]\n")
# shellfish = input("Shellfish?[Y/N]\n")
# fish = input("Fish?[Y/N]\n")
# nuts = input("Tree Nuts?[Y/N]\n")
# wheat = input("Wheat?[Y/N]\n")
# peanuts = input("Peanuts?[Y/N]\n")
# sesame = input("Sesame?[Y/N]\n")
# soybeans = input("Soybeans?[Y/N]\n")


#retreiving data from stored json file
f = open('today.json')
all_menu_items = json.load(f)


#checking current time and assigning a meal period(past 3:00pm--> looking for dinner)
now = datetime.datetime.now()
current_hour = int(now.strftime("%H"))
meal_period = ''
meal_time = ''

if (current_hour>=0 and current_hour<=10):
    meal_period = 'B'
    meal_time = 'Breakfast'
elif (current_hour>10 and current_hour<=15):
    meal_period = 'L'
    meal_time = 'Lunch'
elif (current_hour>15 and current_hour<=21):
    meal_period = 'D'
    meal_time = 'Dinner'

location = 'crossroads'
#find meal period & location that person wants
if location.lower() == 'cafe 3':
    id = f'Cafe3_{meal_period}'
elif location.lower() == 'clark kerr':
    id = f'CK_{meal_period}'
elif location.lower() == 'crossroads':
    id = f'Croads_{meal_period}'
elif location.lower() == 'foothill':
    id = f'FH_{meal_period}'




customer_menu_items = all_menu_items[id]

filtered_menu_items = []

for item in customer_menu_items:
    if milk == "Y" and any("Milk" in label for label in item[5]):
        continue

    if vegan == "Y" and not any('Vegan Option' in label for label in item[5]):
        continue

    if vegetarian == "Y" and not any('Vegetarian Option' in label or 'Vegan Option' in label for label in item[5]):
        continue

    filtered_menu_items.append(item)

print(meal_time + ':')
for item in filtered_menu_items:
    print(','.join(item[:4]))               


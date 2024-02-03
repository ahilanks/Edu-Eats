import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import random
from datetime import date
import datetime
import json



def get_nutrition(data_location, id, menu_id): #function retreives nutritional data that's stored in ajax(dynamically loaded)

    url = 'https://dining.berkeley.edu/wp-admin/admin-ajax.php'
    data = {
        'action': 'get_recipe_details',
        'location': f"{data_location}=",
        'id': f"{id}",
        'menu_id': f"{menu_id}"
    }

    response = requests.post(url, data=data)

    soup = BeautifulSoup(response.text, 'html.parser')

    nutrition_details = soup.find('div', class_='nutration-details sec')

    title_tag = soup.find('h5')
    title = title_tag.get_text(strip=True)

    nutrition_values = {
        item.text.strip(): item.find_next_sibling(string=True).strip()
        for item in nutrition_details.find_all('span')
        if item.text.strip() in ['Calories (kcal):', 'Total Lipid/Fat (g):', 'Protein (g):', 'Carbohydrate (g):']
    }

    calories = nutrition_values.get('Calories (kcal):', 'Not found')
    fat = nutrition_values.get('Total Lipid/Fat (g):', 'Not found')
    protein = nutrition_values.get('Protein (g):', 'Not found')
    carbs = nutrition_values.get('Carbohydrate (g):', 'Not found')

    return title, calories, fat, carbs, protein



def all_menu_items(url, data, locs):
    

    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')

    recip_items = soup.find_all('li', class_=lambda x: x and 'recip' in x) #finds all elements that are menu-items

    n = 0
    temp = recip_items[0].get('data-menuid', 'No data-menuid')

    # Iterate over each item and calling get_nutrtion-- which adds the name and nutrtion info to right location
    for item in recip_items:
        data_location = item.get('data-location', 'No data-location') #fetching all the values(data_loc, data_id, data_menuid from element)
        data_id = item.get('data-id', 'No data-id')
        data_menuid = item.get('data-menuid', 'No data-menuid')

        if temp != data_menuid: #if data_menuid changes, then it is at new location
            n+=1
            temp = data_menuid
        locs[n].append(get_nutrition(data_location, data_id, data_menuid)) #add all the info to appropriate location

    return locs


def dates(date):
    url = 'https://dining.berkeley.edu/wp-admin/admin-ajax.php'
    data = {
        'action': 'cald_filter_xml',
        'date': date
    }
    
    today = datetime.datetime.today()
    if today.weekday() == 5 or today.weekday() == 6: #checks if Saturday or Sunday
        locs = [[], [], [], [], [], [], [], []]
    else:
        locs = [[], [], [], [], [], [], [], [], [], [], [], []]

    return all_menu_items(url, data, locs)

# cafe3_B = 1
# cafe3_L = 2
# cafe3_D = 3
# clark_B = 4
# clark_L = 5
# clark_D = 6
# croads_B = 7
# croads_L = 8
# croads_D = 9
# fh_B = 10
# fh_L = 11
# fh_D = 12



today = date.today().strftime("%Y%m%d")

locs = dates(today) #get all menu_items along with nutrtional info for specific day into right location

print('Welcome to EduEats!')
location = input('Which location are you planning to eat on for this week?\n')
calorie = input('What is your calorie goal?\n')
under_over = input('Are you trying to be under or over that goal?\n')


#based on each location, find the menu_items
if location.lower() == 'cafe 3':
    range_start = 0
elif location.lower() == 'clark kerr':
    range_start = 3
elif location.lower() == 'crossroads':
    range_start = 6
elif location.lower() == 'foothill':
    range_start = 9

breakfast_menu = random.sample(locs[range_start], 5) #randomly give some menu_items
lunch_menu = random.sample(locs[range_start+1], 5)
dinner_menu = random.sample(locs[range_start+2], 5)

print('Breakfast Menu: ', breakfast_menu)
print()
print('Lunch Menu: ', lunch_menu)
print()
print('Dinner Menu: ', dinner_menu)


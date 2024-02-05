import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import random
from datetime import date
import datetime
import json



def get_nutrition(data_location, id, menu_id): #function retreives nutritional data that's stored in ajax(dynamically loaded)


    #reading dietary pref + allergens from original page
    r = requests.get('https://dining.berkeley.edu/menus/', allow_redirects=True) 
    soup = BeautifulSoup(r.text, 'html.parser')
    element = soup.find('li', attrs={"data-id": f"{id}"})
    if element:
        items = element.find_all('span', attrs={"class":"allg-tooltip"})

        labels = []

        for label in items:
            labels.append(label.get_text(strip=True))


    #getting nutritional info from popup
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

    print(title, calories, fat, carbs, protein, labels)
    return title, calories, fat, carbs, protein, labels





def get_all_menu_items(date):
    
    url = 'https://dining.berkeley.edu/wp-admin/admin-ajax.php' 
    data = {
        'action': 'cald_filter_xml',
        'date': date
    }
    
    date_today = datetime.datetime.today()
    if date_today.weekday() == 5 or date_today.weekday() == 6: #checks if Saturday or Sunday and makes respective changes to number of meal periods on that day
        locs = ['Cafe3_B', 'Cafe3_D', 'CK_B', 'CK_D', 'Croads_B', 'Croads_D', 
                 'FH_B', 'FH_D']
        all_items = {'Cafe3_B': [], 'Cafe3_D': [], 'CK_B': [], 'CK_D': [], 'Croads_B': [], 'Croads_D': [], 
                     'FH_B': [], 'FH_D': []}
    else:
        locs = ['Cafe3_B', 'Cafe3_L', 'Cafe3_D', 'CK_B', 'CK_L', 'CK_D', 'Croads_B', 
            'Croads_L', 'Croads_D', 'FH_B', 'FH_L', 'FH_D']
        all_items = {'Cafe3_B': [], 'Cafe3_L': [], 'Cafe3_D': [], 'CK_B': [], 'CK_L': [], 'CK_D': [], 'Croads_B': [], 
                'Croads_L': [], 'Croads_D': [], 'FH_B': [], 'FH_L': [], 'FH_D': []}
        
    response = requests.post(url, data=data) 
    soup = BeautifulSoup(response.text, 'html.parser') # setting up reader

    recip_items = soup.find_all('li', class_=lambda x: x and 'recip' in x) #finds all elements that are menu-items

    n = 0
    temp = recip_items[0].get('data-menuid', 'No data-menuid')

    # Iterate over each item and calling get_nutrtion-- which adds the name and nutrtion info to right location
    for item in recip_items:
        data_location = item.get('data-location', 'No data-location') 
        data_id = item.get('data-id', 'No data-id')
        data_menuid = item.get('data-menuid', 'No data-menuid') #fetching all the values(data_loc, data_id, data_menuid from element)

        if temp != data_menuid: #if data_menuid changes, then it is a new meal/location
            n+=1
            temp = data_menuid
        all_items[locs[n]].append(get_nutrition(data_location, data_id, data_menuid)) #add all the info to appropriate location

    return all_items





today = date.today().strftime("%Y%m%d")

all_menu_items = get_all_menu_items(today) #get all menu_items along with nutrtional info for specific day

with open('today.json', 'w') as f:
  json.dump(all_menu_items, f)


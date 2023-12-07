from bs4 import BeautifulSoup
import requests


def get_nutrtion(data_location, id, menu_id): #function retreives nutrtional data that's stored in ajax(dynamically loaded)

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

    # Now you can access the values from the dictionary
    calories = nutrition_values.get('Calories (kcal):', 'Not found')
    fat = nutrition_values.get('Total Lipid/Fat (g):', 'Not found')
    protein = nutrition_values.get('Protein (g):', 'Not found')
    carbs = nutrition_values.get('Carbohydrate (g):', 'Not found')

    return title, calories, fat, carbs, protein



def all_menu_items():
    locs = [[], [], [], [], [], [], [], [], [], [], [], []]

    r = requests.get('https://dining.berkeley.edu/menus/', allow_redirects=True) #initalizing beautiful soup to read text
    soup = BeautifulSoup(r.text, 'html.parser')

    recip_items = soup.find_all('li', class_=lambda x: x and 'recip' in x)

    n = 0
    temp = recip_items[0].get('data-menuid', 'No data-menuid')

    # Iterate over each item and print its 'data-id' and 'data-menuid'
    for item in recip_items:
        data_location = item.get('data-location', 'No data-location')
        data_id = item.get('data-id', 'No data-id')
        data_menuid = item.get('data-menuid', 'No data-menuid')
        if temp != data_menuid:
            n+=1
            temp = data_menuid
        locs[n].append(get_nutrtion(data_location, data_id, data_menuid))

    return locs


cafe3_B = 1
cafe3_L = 2
cafe3_D = 3
clark_B = 4
clark_L = 5
clark_D = 6
croads_B = 7
croads_L = 8
croads_D = 9
fh_B = 10
fh_L = 11
fh_D = 12


print(all_menu_items()[fh_D])

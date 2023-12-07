import requests
from bs4 import BeautifulSoup


def get_nutrtion(data_location, id, menu_id):

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

print(get_nutrtion('aHR0cHM6Ly9kaW5pbmcuYmVya2VsZXkuZWR1L3dwLWNvbnRlbnQvdXBsb2Fkcy94bWxfZmlsZXMvQ3Jvc3Nyb2Fkc18yMDIzMTIwNi54bWw', 3331347, 8532))

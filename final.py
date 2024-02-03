from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time



# r = requests.get('https://dining.berkeley.edu/menus/', allow_redirects=True) #initalizing beautiful soup to read text
# soup = BeautifulSoup(r.text, 'html.parser')

# cal_dining = {'Cafe 3': 8615, 
#             'Clark Kerr': 8587, 
#             'Crossroads': 8531, 
#             'Foothill': 8566}


# for key, value in cal_dining.items(): 
#     elements = soup.find_all('li', attrs={"data-menuid": f"{value}"}) #find all elements of a particular location
#     menu_items = {}
#     for element in elements: 
#         # Find the <span> within the current <li> element
#         menu_item = element.find('span')
#         if menu_item:  # Check if a <span> tag was found
#             # Get the text, strip leading/trailing whitespace, and add it to the list
#             menu_items[menu_item.get_text(strip=True)] = []

#     cal_dining[key] = menu_items

# print(cal_dining)


id = '5637076'

r = requests.get('https://dining.berkeley.edu/menus/', allow_redirects=True) 
soup = BeautifulSoup(r.text, 'html.parser')
element = soup.find('li', attrs={"data-id": f"{id}"})

items = element.find_all('span', attrs={"class":"allg-tooltip"})

labels = []

for label in items:
    labels.append(label.get_text(strip=True))


print(labels)
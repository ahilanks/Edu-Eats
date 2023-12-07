from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import re


# driver = webdriver.Chrome() #initializing driver
# driver.get('https://dining.berkeley.edu/menus/') 
# time.sleep(2)

# dropdown = driver.find_elements(By.CLASS_NAME, 'accordion-icon') #clicking arrow to open menu items(don't think I really need this)
# dropdown[8].click()
# time.sleep(2)

# items = driver.find_elements(By.XPATH, "//li[@data-menuid='8532']") #clicking on item to open nutrtion info popup
# items[0].click()
# time.sleep(5)


r = requests.get('https://dining.berkeley.edu/menus/', allow_redirects=True) #initalizing beautiful soup to read text
soup = BeautifulSoup(r.text, 'html.parser')

recip_items = soup.find_all('li', class_=lambda x: x and 'recip' in x)


# Iterate over each item and print its 'data-id' and 'data-menuid'
for item in recip_items:
    data_location = item.get('data-location', 'No data-location')
    data_id = item.get('data-id', 'No data-id')
    data_menuid = item.get('data-menuid', 'No data-menuid')
    print(f"Data Location: {data_location} Data ID: {data_id}, Data Menu ID: {data_menuid}")




"""elements = soup.find_all(lambda tag: tag.has_attr('data-menuid') and tag['data-menuid'] == '8531') # Extract 'data-id' from specific meal period & location
data_ids = [element['data-id'] for element in elements if 'data-id' in element.attrs]


desired_id = data_ids[0]"""

"""element = element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f".cald-popup-wrapper.show a[id='{desired_id}']")))
print(element)"""

"""menu_items_clickable = driver.find_elements(By.XPATH, "//li[@data-id='4861352']")

menu_items_clickable[0].click()





crossroads_dinner = soup.find_all('li', attrs={'data-menuid': '8531'})
span_texts = []

for item in crossroads_dinner: # get texts from 
    # Find the <span> within the current <li> element
    span = item.find('span')
    if span:  # Check if a <span> tag was found
        # Get the text, strip leading/trailing whitespace, and add it to the list
        span_texts.append(span.get_text(strip=True))

print(span_texts)
time.sleep(1000)"""





"""def get_page_links(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    items = sp.select(driver.find)"""
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


driver = webdriver.Chrome() #initializing driver
driver.get('https://dining.berkeley.edu/menus/') 
time.sleep(2)

dropdown = driver.find_elements(By.CLASS_NAME, 'accordion-icon') #clicking arrow to open menu items(don't think I really need this)
dropdown[5].click()
time.sleep(2)

items = driver.find_elements(By.XPATH, "//li[@data-menuid='8531']") #clicking on item to open nutrtion info popup
items[0].click()
time.sleep(5)



"""recipe_details = driver.find_elements(By.CLASS_NAME, 'nutration-details sec') #using driver to get info
print(recipe_details)"""





r = requests.get('https://www.google-analytics.com/g/collect?v=2&tid=G-F4NTEFFFMS&gtm=45je3bt0v867550927&_p=1701672984185&gcd=11l1l1l1l1&dma=0&cid=1167818207.1692407257&ul=en-us&sr=1470x956&uaa=arm&uab=64&uafvl=Google%2520Chrome%3B119.0.6045.199%7CChromium%3B119.0.6045.199%7CNot%253FA_Brand%3B24.0.0.0&uamb=0&uam=&uap=macOS&uapv=14.1.1&uaw=0&are=1&_eu=AEA&_s=8&sid=1701672386&sct=41&seg=1&dl=https%3A%2F%2Fdining.berkeley.edu%2Fmenus%2F&dt=Menus%20-%20Dining&en=click&ep.link_id=4734450&ep.link_classes=cald-close&ep.link_url=javascript%3Avoid(0)&ep.link_domain=&ep.outbound=true&_et=13763&tfd=917020', allow_redirects=True) #initalizing beautiful soup to read text
soup = BeautifulSoup(r.text, 'html.parser')


print(soup)
# recipe_details = soup.find('div', class_='recipe-details')

# print(recipe_details)
"""nutrition_details = recipe_details.find('div', class_ = 'nutration-details sec')
nutrition_facts = nutrition_details.find('ul')  # Assuming the <ul> contains the nutrition facts

# Find the <li> element that contains the Calories information
calories_li = nutrition_facts.find('li', text=lambda t: 'Calories' in t)

# Assuming the number follows the Calories label within the same <li> tag
calories = calories_li.find('span').next_sibling.strip()

print(f"Calories: {calories}")"""

##lipids = nutrition_details.find("span", text="Total Lipid/Fat (g):").find_next_sibling().text
##carbs = nutrition_details.find("span", text="Carbohydrate (g):").find_next_sibling().text
##protein = nutrition_details.find("span", text="Protein (g):").find_next_sibling().text

"""print(f"Calories: {calories}")
print(f"Lipids: {lipids}")
print(f"Carbohydrates: {carbs}")
print(f"Protein: {protein}")"""



time.sleep(1000)









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
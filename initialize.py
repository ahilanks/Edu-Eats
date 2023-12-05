from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Constants
DINING_URL = "https://dining.berkeley.edu/menus/"
CROSSROADS_SECTION = 'ACTUAL_SELECTOR_FOR_CROSSROADS'
DATE_DROPDOWN = 'ACTUAL_SELECTOR_FOR_DATE_DROPDOWN'
DATE_OPTION = 'ACTUAL_SELECTOR_FOR_DATE_OPTION'
MENU_ITEMS = 'ACTUAL_SELECTOR_FOR_MENU_ITEMS'
DAYS_TO_SCRAPE = 7  # Assuming you want to scrape a week's worth of data

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get(DINING_URL)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, CROSSROADS_SECTION)))

# Navigate to Crossroads
driver.find_element(By.CSS_SELECTOR, CROSSROADS_SECTION).click()

# Initialize a pandas DataFrame
df = pd.DataFrame()

# Scrape menus for the number of days required
for i in range(DAYS_TO_SCRAPE):
    # Open the date dropdown and select the date
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, DATE_DROPDOWN))).click()
    time.sleep(1)  # Adjust sleep time as necessary
    date_options = driver.find_elements(By.CSS_SELECTOR, DATE_OPTION)
    
    # Click the specific date option
    date_options[i].click()
    
    # Wait for menu items to load
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, MENU_ITEMS)))
    
    # Get the menu items using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    menu_list = soup.select(MENU_ITEMS)
    
    # Extract the text and store in DataFrame
    date_text = date_options[i].text  # Assuming the date is the text of the option
    df[date_text] = [item.get_text() for item in menu_list]

# Clean up by closing the browser
driver.quit()

# Save the DataFrame to CSV
df.to_csv('menu_items.csv', index=False)

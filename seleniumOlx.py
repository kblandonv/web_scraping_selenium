# This script is used to scrape the data from the OLX website
# The data that we are going to scrape is the title, price and description of the car
# The data is going to be stored in a list of dictionaries
# Author: kblandonv

import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Path to the edge driver
driver = webdriver.Edge('./msedgedriver.exe')

# Open the browser
driver.get('https://www.olx.com.co/carros_c378')

button = driver.find_element(by=By.XPATH, value='//button[@data-aut-id="btnLoadMore"]')

# wait for button to be clickable
for i in range(3):

    try:
        # Click the button
        button.click()
        # wait for button to be clickable
        sleep(random.uniform(8.0, 10.0))
        button = driver.find_element(by=By.XPATH, value='//button[@data-aut-id="btnLoadMore"]')
    except:
        break
    
# Get the list of cars
cars = driver.find_elements(by=By.XPATH, value='//li[@data-aut-id="itemBox"]')


# Iterate over the list of cars
for car in cars:
    # Get the title of the car
    title = car.find_element(by=By.XPATH, value='.//span[@data-aut-id="itemTitle"]').text
    print(title)
    # Get the price of the car
    price = car.find_element(by=By.XPATH, value='.//span[@data-aut-id="itemPrice"]').text
    print(price)
    # Get the description of the car
    description = car.find_element(by=By.XPATH, value='.//span[@data-aut-id="itemDetails"]').text
    print(description)
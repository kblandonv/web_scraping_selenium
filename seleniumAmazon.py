
# Description: This script will allow us to scrape the data from the amazon website
# The data that we are going to scrape is the title, price, rating and number of reviews of the product
# The data is going to be stored in a excel file
# Author: kblandonv

import os
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Path to the edge driver
PATH = './msedgedriver.exe'
driver = webdriver.Edge(PATH)
# Open the browser
driver.get('https://www.amazon.com/')
driver.maximize_window()

# Search for the product
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.clear()
search_box.send_keys('asus laptop')
driver.find_element(By.ID, 'nav-search-submit-button').click()

driver.find_element(By.XPATH, '//span[text()="ASUS"]').click()

# Define the lists
laptop_names = []
laptop_prices = []
laptop_ratings = []
laptop_reviews = []


# Get the list of products
all_products = driver.find_elements(
    By.XPATH, '//div[@data-component-type="s-search-result"]')

for product in all_products:

    # Iterate over the list of products
    # Name of the product
    names = product.find_elements(
        By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
    for name in names:
        laptop_names.append(name.text)

    # Price of the product
    prices = product.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
    for price in prices:
        laptop_prices.append(price.text)

    # Rating of the product
    ratings = product.find_elements(By.XPATH, './/span[@class="a-size-base"]')
    for rating in ratings:
        laptop_ratings.append(rating.text)

    # Review of the product
    try:
        if len(product.find_elements(By.XPATH, './/span[@class="a-size-base s-underline-text"]')) > 0:
            reviews = product.find_elements(
                By.XPATH, './/span[@class="a-size-base s-underline-text"]')
            for review in reviews:
                laptop_reviews.append(review.text)
        else:
            laptop_reviews.append('No reviews')
    except:
        pass

print('name===>', len(laptop_names))
print('price===>', len(laptop_prices))
print('rating===>', len(laptop_ratings))
print('reviews===>', len(laptop_reviews))


# Create a dataframe
df = pd.DataFrame(zip(laptop_names, laptop_prices, laptop_ratings,
                  laptop_reviews), columns=['Name', 'Price', 'Rating', 'Reviews'])
# Save the dataframe to a excel file
df.to_excel(
    r"C:\Users\kevin\Documents\web_scraping_selenium\Tables\laptops_list.xlsx", index=False)

# Open the file
os.system(r'start "excel" "C:\Users\kevin\Documents\web_scraping_selenium\Tables\\laptops_list.xlsx"')

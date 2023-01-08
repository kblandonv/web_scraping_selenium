
# Description: This script will log into twitter and get the tweets of a specific subject
# The data that we are going to scrape is username, tweet, date and time, likes, retweets, and replies
# The data is going to be stored in a excel file
# Author: kblandonv

import os
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import getpass as gp  # To hide the password

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Path to the edge driver
driver = webdriver.Edge('./msedgedriver.exe', options=opts)

# Open twitter
driver.get('https://twitter.com/login')
driver.maximize_window()

subject = 'FastApi'

# Set the username
# Wait for the page to load
sleep(3)
# Find the username input
username = driver.find_element(by=By.XPATH, value='//input[@name="text"]')
username.send_keys('username')

# Next button
nextButton = driver.find_element(
    by=By.XPATH, value='//span[contains(text(), "Siguiente")]')
nextButton.click()

# Set the password
# Wait for the page to load
sleep(3)
# Find the password input
password = driver.find_element(by=By.XPATH, value='//input[@name="password"]')
password.send_keys('password')
loginButton = driver.find_element(
    by=By.XPATH, value='//span[contains(text(), "Iniciar sesión")]')
loginButton.click()

# Search item and click on it
# Wait for the page to load
sleep(3)
# Find the search input
search = driver.find_element(
    by=By.XPATH, value='//input[@data-testid="SearchBox_Search_Input"]')
search.send_keys(subject)
search.send_keys(Keys.ENTER)

sleep(5)
# Click on persons
people = driver.find_element(
    by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span')
people.click()

sleep(5)
# Click on the first person
profile = driver.find_element(
    by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span')
profile.click()

sleep(3)
# Get the name of the user
userTag = driver.find_element(
    by=By.XPATH, value='//div[@data-testid="User-Names"]').text
# Get the date of the tweet
TimeStamp = driver.find_element(
    by=By.XPATH, value='//time').get_attribute('datetime')
# Get the tweet
Tweet = driver.find_element(
    by=By.XPATH, value='//div[@data-testid="tweetText"]').text
# Get the number of replies
Replies = driver.find_element(
    by=By.XPATH, value='//div[@data-testid="reply"]')
# Get the number of retweets
Retweets = driver.find_element(
    by=By.XPATH, value='//div[@data-testid="retweet"]')
# Get the number of likes
Likes = driver.find_element(
    by=By.XPATH, value='//div[@data-testid="like"]')

userTags = []
timeStamps = []
tweets = []
replies = []
retweets = []
likes = []

# Get article
articles = driver.find_elements(
    by=By.XPATH, value='//article[@data-testid="tweet"]')
while True:
    for article in articles:
        # Get the name of the user
        userTag = article.find_element(
            by=By.XPATH, value='.//div[@data-testid="User-Names"]').text
        userTags.append(userTag)
        # Get the date of the tweet
        TimeStamp = article.find_element(
            by=By.XPATH, value='.//time').get_attribute('datetime')
        timeStamps.append(TimeStamp)
        # Get the tweet
        Tweet = article.find_element(
            by=By.XPATH, value='.//div[@data-testid="tweetText"]').text
        tweets.append(Tweet)
        # Get the number of replies
        Replies = article.find_element(
            by=By.XPATH, value='.//div[@data-testid="reply"]').text
        replies.append(Replies)
        # Get the number of retweets
        Retweets = article.find_element(
            by=By.XPATH, value='.//div[@data-testid="retweet"]').text
        retweets.append(Retweets)
        # Get the number of likes
        Likes = article.find_element(
            by=By.XPATH, value='.//div[@data-testid="like"]').text
        likes.append(Likes)
        print(userTag, TimeStamp, Tweet, Replies, Retweets, Likes)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    articles = driver.find_elements(
        by=By.XPATH, value='//article[@data-testid="tweet"]')
    tweets_list = list(set(tweets))
    if len(tweets_list) > 5:
        break

print(len(userTags), len(timeStamps), len(tweets),
      len(replies), len(retweets), len(likes))

# Create a dataframe
df = pd.DataFrame(zip(userTags, timeStamps, tweets, replies, retweets, likes), columns=[
                  'User', 'Date', 'Tweet', 'Replies', 'Retweets', 'Likes'])
df.head()
# Save the file
df.to_excel(r"C:\Users\kevin\Documents\web_scraping_selenium\Tables\tweets_list.xlsx", index=False)
# Open the file
os.system(r'start "excel" "C:\Users\kevin\Documents\web_scraping_selenium\Tables\\tweets_list.xlsx"')
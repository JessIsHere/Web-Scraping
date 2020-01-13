#!/usr/bin/env python
# coding: utf-8

# Import dependencies:

from splinter import Browser
from bs4 import BeautifulSoup 
import pprint


# Splinter Path:

driverPath = get_ipython().getoutput('which chromedriver')
executable_path = {'executable_path': driverPath[0]}
browser = Browser('chrome', **executable_path, headless=False) 


# Navigate to website

url = 'https://mars.nasa.gov/news'
browser.visit(url)
html = browser.html


#Create BeautifulSoup Object

soup = BeautifulSoup(html, 'html.parser')


#Find first article name and text. Store

article_list = soup.find(class_='slide')
title = article_list.find('h3').text
title_p = article_list.find(class_='article_teaser_body').text

#Check Correct

print(title)
print(title_p)


# Navigate to website

space_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(space_image)


# Pull image using splinter:
image_find = browser.find_by_id('full_image')

#Check Correct
image_find.click()


# Navigate to website:

tweet_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(tweet_url)


# In[64]:


#I know this is fucking right why isnt it working
first_container = soup.find('p','tweet-text').get_text()






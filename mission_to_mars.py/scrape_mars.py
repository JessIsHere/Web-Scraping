#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import html
import pandas as pd
import pprint
import requests


# In[2]:

def scrape():
    driverPath = get_ipython().getoutput('which chromedriver')
    executable_path = {'executable_path': driverPath[0]}
    browser = Browser('chrome', **executable_path, headless=False) 


    # In[3]:


    #Create BeautifulSoup Object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[164]:


    url = 'https://mars.nasa.gov/news'
    browser.visit(url)


    # In[166]:  


    #Find first article name and text. Store 
    article_list = soup.find(class_='slide')
    news_title = article_list.find('h3').text
    news_p = article_list.find(class_='article_teaser_body').text
    # Check that it works
    print(news_title)
    print(news_p)

    # In[131]:

    space_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(space_image)
    image = browser.find_by_tag('article')


    # In[132]:

    featured_image_url = browser.find_by_id('full_image')

    # In[133]:

    #Splinter to pull tweet
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tweet_url)

    # In[134]:

    timeline = browser.find_by_id("timeline")
    timeline.click()

    # In[135]:

    # Python to scrape facts
    facts_url= requests.get('https://space-facts.com/mars/')
    bsfacts = BeautifulSoup(facts_url.text)
    print(bsfacts)


    # In[136]:

    facts_table = bsfacts.find(id='text-2').text
    print(facts_table)

    # In[148]:


    # In[141]:

    img_find = browser.find_by_css('img')
    img_click = img_find.find_by_css('thumb')


    # In[7]:


    import requests
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome()
    driver.get('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


    # In[27]:


    imgElement = driver.find_element_by_class_name('thumb');
    imgElement.click()
    new_driver = driver.current_url
    downloads = new_driver.find_element_by_class_name('downloads')
    image = downloads.find_element_by_tag_name('href')





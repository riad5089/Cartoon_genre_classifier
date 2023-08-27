#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import selenium
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium import webdriver

# path = r'C:\Users\Abdur rahim nishad\Mastercourse\chromedriver.exe'
# from selenium import webdriver

path = r'C:\Users\Abdur rahim nishad\Mastercourse\chromedriver.exe'
options = webdriver.ChromeOptions()
# Set any desired options using options.add_argument()
# For example:
# options.add_argument("--headless")  # Run Chrome in headless mode

service = webdriver.chrome.service.Service(path)
service.start()

browser = webdriver.Chrome(service=service, options=options)
title=[]
genre=[]
des=[]
browser.get("https://www.animegg.org/popular-series?sortBy=hits&sortDirection=DESC&ongoing&limit=25&start=1")
for i in range(1,701):
    browser.get(f"https://www.animegg.org/popular-series?sortBy=hits&sortDirection=DESC&ongoing&limit=25&start={i}")
    for i in range(1,56):
        try:
            browser.find_element(By.XPATH,f"//*[@id='popularAnime']/li[{i}]/div[2]/a").click()
        except:
            continue
        try:
            title.append(browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/h1').text)
        except:
            title.append(np.nan)
        try:
            des.append(browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/p").text)
        except:
            des.append(np.nan)
        browser.execute_script("window.history.go(-1)")

#         sleep(5)
#         browser.back() 

    
        
        genres=[]
        counter = 1
        genres_found = True

        while genres_found:
            try:
                # Construct the XPath with the counter variable
                xpath =f"//*[@id='popularAnime']/li[{i}]/div[2]/div/ul[2]/li[{counter}]/a"

                # Find the elements using the XPath
                elements = browser.find_elements(By.XPATH, xpath)

                # Check if any elements were found
                if elements:
                    # Process the elements
                    for element in elements:
                        # Perform the desired operations on each genre element
                        # Replace newline characters with commas
                        li = element.text.replace('\n', ', ')
                        # Print the modified genre string
                        try:
                            genres.append(li)
                        except:
                            genres.append(np.nan)
                else:
                    # No genres found, exit the loop
                    genres_found = False

                # Increment the counter for the next iteration
                counter += 1

            except Exception as e:
                # Handle any exceptions that occur during scraping
                print("Error:", e)
                break
        genre.append(genres)
        data = {
                'Title': title,
                'Description': des,
                'Genre': genre
                }
        df = pd.DataFrame(data)
        df.to_csv("new_cartoon.csv", index=False)


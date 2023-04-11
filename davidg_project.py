# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:39:42 2023

@author: DavidG
"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv

urlText1='https://www.beersmith.com/Recipes2/recipe_'
urlText2='.htm'
url=''

for counter  in range(0,2):
    url= urlText1+str(counter)+urlText2
    
    page=requests.get(url)
    driver=webdriver.Chrome()
    driver.get(url) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    table = soup.find('table', id='table1') 
 
    file = open("project2.csv", "a")
    writer = csv.writer(file)

    writer.writerow(["Amount","Item","Type","IBU"])  

    index=0
    for table in table.tbody.find_all('table'):    
        for row in table.tbody.find_all('tr'):
            data=[]
            for columns in row.find_all('td'):
                if (columns != []):
                    data.append(columns.text.strip())

            if data !=[]:
                #print(data)
                writer.writerow(data)
    
    import time
    time.sleep(5) 
           
driver.close()
file.close()
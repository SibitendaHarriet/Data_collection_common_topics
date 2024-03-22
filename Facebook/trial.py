# Import the required modules 

import getpass
import os
import click 
import selenium 
from selenium import webdriver 
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import random
import time 
import requests

import re
from time import sleep
from datetime import datetime
import xlsxwriter
import pandas as pd

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")


# Specify the facebooks URL 
url = "https://facebook.com"

# Specify credentials
current_user = getpass.getuser() 
driver_path = "chromedriver.exe"
input_username = "xxxx@gmail.com"
input_key = "******"
# Define the web driver and point it to the url of interest
driver = webdriver.Chrome(executable_path=driver_path, options=option)
driver.get(url)
# Log in to the url using the given credentials
element= driver.find_element(by=By.ID, value= "email")
element.send_keys(input_username)
element= driver.find_element(by=By.ID, value="pass")
element.send_keys(input_key)
element.send_keys(Keys.RETURN)

driver.implicitly_wait(10)
group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202018%20' 
driver.get(group) 
time_list=[]
username_list=[]

while True:
    soup=BeautifulSoup(driver.page_source,"html.parser")#, options=option)
    all_posts=soup.find_all("div",{"class":"x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld"})                                      

    for post in all_posts:
        #print(post)
        try:
            time=post.find("span",{"class":"x1lliihq x6ikm8r x10wlt62 x1n2onr6"}).text
        except:
            time="not found"
        print(time)    
         
        try:
            username=post.find("span",{"class":"xuxw1ft"}).text 
        
        except:
            username="not found"
        print(username)
        
        time_list.append(time)
        username_list.append(username)
       
        df=pd.DataFrame({"time":time_list,"username":username_list})
        df.drop_duplicates(subset ="title",keep ="first", inplace = True)

        df.to_excel("./facebook/fb_concerns.xlsx")

        if df.shape[0]>1000:
            break
    if df.shape[0]>1000:
        break
sleep(5)
y=500
for timer in range(0,10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    y+=500
    sleep(3)


#     #driver.get(soup)




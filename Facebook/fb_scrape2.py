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

if not current_user =='pilgrim':
    # Define resources to be used in the program 
    driver_path = "chromedriver.exe"
    input_username = "xxx@gmail.com"
    input_key = "xxx"  
else:
    # Define resources to be used in the program 
    driver_path = "chromedriver101.exe"
    input_username = "xxxx@gmail.com"
    input_key = "PB21@pilgrim" 

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

#group = 'https://web.facebook.com/search/videos/?q=social%20concerns%2C%20africa%2C%202020%20' 
group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202018%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20concerns%2C%20africa%2C%202022%20' 

#group = 'https://web.facebook.com/search/videos/?q=social%20problems%2C%20africa%2C%202018%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20problems%2C%20africa%2C%202019%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20problems%2C%20africa%2C%202020%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20problems%2C%20africa%2C%202021%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20problems%2C%20africa%2C%202022%20' 

#group = 'https://web.facebook.com/search/videos/?q=social%20challenges%2C%20africa%2C%202018%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20challenges%2C%20africa%2C%202019%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20challenges%2C%20africa%2C%202020%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20challenges%2C%20africa%2C%202021%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20challenges%2C%20africa%2C%202022%20' 


#group = 'https://web.facebook.com/search/videos/?q=social%20issues%2C%20africa%2C%202018%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20issues%2C%20africa%2C%202019%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20issues%2C%20africa%2C%202020%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20issues%2C%20africa%2C%202021%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20issues%2C%20africa%2C%202022%20' 

#group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202018%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202019%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202020%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202021%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20questions%2C%20africa%2C%202022%20' 

#group = 'https://web.facebook.com/search/videos/?q=social%20worry%2C%20africa%2C%202018%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20worry%2C%20africa%2C%202019%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20worry%2C%20africa%2C%202020%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20worry%2C%20africa%2C%202021%20' 
#group = 'https://web.facebook.com/search/videos/?q=social%20worry%2C%20africa%2C%202022%20' 



driver.get(group) 

time_list=[]
username_list=[]
title_list=[]
desc1_list=[]
desc2_list=[]
reactions_list=[]
links_list=[]

while True:
    soup=BeautifulSoup(driver.page_source,"html.parser")#, options=option)
    all_posts=soup.find_all("div",{"class":"x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld"})                                      

    for post in all_posts:
        #print(post)
        try:
            title=post.find("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1s688f"}).get('aria-label')
        except:
            title="not found"
        print(title) 
        try:
            links=post.find("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1s688f"}).get('href')
        except:
            links="nolinks"
        print(links)
        try:
            desc1=post.find("span",{"class":"x1lliihq x6ikm8r x10wlt62 x1n2onr6 x1j85h84"}).text 
        except:
            desc1="not found"
        print(desc1)
        try:
            desc2=post.find("span",{"class":"x1lliihq x6ikm8r x10wlt62 x1n2onr6"}).text
        except:
            desc2="not found"
        print(desc2)
        try:
            time=post.find("span",{"class":"x1lliihq x6ikm8r x10wlt62 x1n2onr6"}).text
        except:
            time="not found"
        print(time)    
        try:
            reactions=post.find("span",{"class":"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1nxh6w3 x1sibtaa xo1l8bm xi81zsa"}).text
        except:
            reactions="no reactions"
        print(reactions)
        try:
            username=post.find("span",{"class":"xuxw1ft"}).text 
        
        except:
            username="not found"
        print(username)
        
        time_list.append(time)
        username_list.append(username)
        title_list.append(title)
        desc1_list.append(desc1)
        desc2_list.append(desc2)
        reactions_list.append(reactions)
        links_list.append(links)

        df=pd.DataFrame({"time":time_list,"links_ID":links_list,"username":username_list,"title":title_list,"desc1":desc1_list,"desc2":desc2_list,"reactions":reactions_list})
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




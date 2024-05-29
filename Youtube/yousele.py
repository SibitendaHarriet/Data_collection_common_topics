from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import re
from time import sleep
from datetime import datetime
import xlsxwriter
import pandas as pd

#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait

driver_path = "chromedriver101.exe"
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path=driver_path, options=option) 

for i in range(1,2): # Iterate from page 1 to the last page
    #browser.get("https://tw.mall.yahoo.com/search/product?p=%E5%B1%88%E8%87%A3%E6%B0%8F&pg={}".format(i))
    driver.get("https://www.youtube.com/results?search_query=social+questions%2C+Africa%2C+2022".format(str(i)))
    #test = read_youtube(["concern", "problem", "challenge", "worry", "issue", "question"], 2021, 2022)

    user_data = driver.find_elements(By.XPATH,'//*[@id="video-title"]')
    links = []
    for i in user_data:
            links.append(i.get_attribute('href'))

    print(len(links))
time_list=[]
username_list=[]
title_list=[]
desc1_list=[]
desc2_list=[]
reactions_list=[]
links_list=[]

while True:
    soup=BeautifulSoup(driver.page_source,"html.parser")#, options=option)
    all_posts=soup.find_all("ytd-video-renderer",{"class":"style-scope ytd-item-section-renderer"})                                      

    for post in all_posts:
        #print(post)
        try:
            title=post.find("a",{"class":"yt-simple-endpoint style-scope ytd-video-renderer"}).get('aria-label')
        except:
            title="not found"
        print(title) 
        try:
            links=post.find("a",{"class":"yt-simple-endpoint style-scope ytd-video-renderer"}).get('href')
        except:
            links="nolinks"
        print(links)
        try:
            desc1=post.find("span",{"class":"style-scope yt-formatted-string"}).text
        except:
            desc1="not found"
        print(desc1)
        try:
            desc2=post.find("span",{"class":"style-scope ytd-promoted-video-renderer"}).text
        except:
            desc2="not found"
        print(desc2)
        try:
            time=post.find("span",{"class":"inline-metadata-item style-scope ytd-video-meta-block"}).text
        except:
            time="not found"
        print(time)    
        try:
            reactions=post.find("div",{"class":"inline-metadata-item style-scope ytd-video-meta-block"}).text
        except:
            reactions="no reactions"
        print(reactions)
        try:
            username=post.find("a",{"class":"yt-simple-endpoint style-scope yt-formatted-string"}).text 
        
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

        df.to_excel("youquestions.xlsx")

        if df.shape[0]>1000:
            break
    if df.shape[0]>1000:
        break
sleep(5)
y=500
for timer in range(0,1000):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    y+=500
    sleep(3)


#     #driver.get(soup)




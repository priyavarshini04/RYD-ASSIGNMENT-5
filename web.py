from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.indiabix.com/current-affairs/state/")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'bix-div-container'}):
    QUESTION=a.find('div', attrs={'class':'bix-td-qtxt'})
    OPTIONS=a.find('div', attrs={'class':'bix-tbl-options'})
    ANSWER=a.find('div', attrs={'class':'jq-hdnak mx-bold'})
QUESTION.append(QUESTION.text)
OPTIONS.append(OPTIONS.text)
ANSWER.append(ANSWER.text)

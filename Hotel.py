from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/vijay/Downloads/chromedriver_win32/chromedriver")
hotels=[]
prices=[]
driver.get("https://www.makemytrip.com/hotels/hotel-listing/?checkin=10022020&city=CTXDB&checkout=11022020&roomStayQualifier=2e0e&locusId=CTXDB&country=IN&locusType=city&searchText=Hubli,%20India&visitorId=7398d6b4-9b03-4acd-bd8d-ac62dad83ce3")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div', attrs={'class':'makeFlex spaceBetween'}):
    name=a.find('p', attrs={'class':'latoBlack font22 blackText appendBottom12'})
    hotels.append(name.text)
for a in soup.findAll('div', attrs={'class':'padding20 makeFlex column'}):
    price=a.find('p', attrs={'class':'latoBlack font26 blackText appendBottom5'})
    prices.append(price.text)
    
df = pd.DataFrame({'Hotel Name':hotels,'Price':prices}) 
df.to_csv('Hotels.csv', index=False, encoding='utf-8')
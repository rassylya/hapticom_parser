from lxml import html
from bs4 import  BeautifulSoup
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def proxyParser():
    proxies = ()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://scrapingant.com/free-proxies/")
    sleep(7)    
    sourceCode=driver.page_source
    soup = BeautifulSoup(sourceCode,'lxml')
    table = soup.find("table", class_="proxies-table")
    rows = table.find_all("tr")
    for i in range(1,11):
        column = rows[i]
        tds = column.find_all("td")
        proxy = f"http://{tds[0].string}:{tds[1].string}"
        proxies = proxies + (proxy,)
    print(proxies)
    return proxies
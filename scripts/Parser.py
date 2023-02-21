from bs4 import BeautifulSoup
from urllib.request import urlopen
# from api import get_scrapeops_url
from GetProxy import getProxy
import requests
from Signs import special_signs
import urllib

filename = ''

def writer(m,f,i=0,j=0):
    text = m.get_text()
    textL = list(text)
    text = ''
    for t in textL:
        if t in special_signs.keys():
            t = special_signs[t]
        text = text + t
    # print(text)
    if m.name and m.name.startswith('h'):    
        f.write(f"Header: {text}\n")
    elif m.name and m.find('th'):
        i += 1
        f.write(f"Table Header #{i}: {text}\n")
    elif m.name and m.find('tr'):
        j += 1
        f.write(f"Row #{j}: {text}\n")    
    else:
        f.write(f"{text}\n")
    
def parser(url):
    try:
        page = requests.get(url=url)
    except HTTPError as e:
        print("The site using web scrapper, trying to use proxy to avoid")
        if e.code == 403:
            proxy = getProxy(url)
            page = requests.get(url=url, proxies={"http": proxy, "https": proxy})
    
    soup = BeautifulSoup(page.content, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    global filename
    filename = soup.title.string
    Fname = list(filename)
    filename = ''
    for letter in Fname:
        if letter in special_signs.keys():
            letter = special_signs[letter]
        filename = filename + letter
    f = open(f"../Parsed_Files/{filename}.txt", "w") or open(f"Parsed_Files/{filename}.txt", "w")  
    f.write(f"Title: {filename}")


    classes = soup.find_all(class_=True)
    ids = soup.find_all(id=True)
    # container = soup.find_all("div", class_="c")
    main = soup.find("main")
    main1 = []
    if main is not None:
        for m in main:
            writer(m,f)
            
    elif main is None and classes:
        for i in classes:
            for j in i['class']:
                if 'main' in j or 'content' in j:
                    print('main class found')
                    main1.append(i)
    elif main is None and ids:
        for i in ids:
            if 'main' in i['id']:
                print('main id found')
                main1.append(i)
    if main1:    
        for m in main1:
            for l in m:
                writer(m,f)
            
    f.close()

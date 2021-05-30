import os
import shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#url = "https://www.chrisburkard.com/"
url = "https://www.mercadolibre.com.ar/"
web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, "html.parser")

print(len(web_soup.findAll("img")))

#gecko_path = "C:\Dev\practica\scraping\geckodriver.exe"
#driver = webdriver.Firefox(gecko_path)
#driver = webdriver.Firefox()
driver = webdriver.Firefox()
driver.get(url)

iterations = 0
while iterations < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html, "html.parser")
    print(len(sel_soup.findAll("img")))
    images = []
    for i in sel_soup.findAll("img"):
        print(i)
        src = i["src"]
        images.append(src)

    print(images)
    current_path = os.getcwd()
    for img in images:
        try:
            file_name = os.path.basename(img)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "images", file_name)
            with open(new_path, "wb") as output_file:
                shutil.copyfileobj(img_r.raw, output_file) #wb "write binary" porque estoy tomando el .raw de los datos de la imagen
            del img_r
        except:
            pass

    iterations += 1
    time.sleep(5)

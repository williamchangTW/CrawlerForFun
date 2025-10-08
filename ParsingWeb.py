'''
Author: williamchangTW
Purpose: Get the 康熙字典 content of https://1788lu.com/
'''
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# Target URL
#url = "https://1788lu.com/name-rename/name-and-glossology/11-strokes-of-kangxi-dictionary.html"
url = "https://1788lu.com/name-rename/name-and-glossology/10-strokes-of-kangxi-dictionary.html"
'''
# selenium
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

soup = bs(driver.page_source, "html.parser")

for e in soup.select("#i20d421aa6409 > div > div"):
    print(e.get_text(strip=True))
'''

driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)  # 等待 JS 載入

soup = bs(driver.page_source, "html.parser")

tables = soup.select("section table.naming-strokes-table")

data = []
for table in tables:
    rows = table.select("tbody tr")
    for row in rows:
        cols = [td.get_text(strip=True) for td in row.select("td")]
        data.append(cols)
        #print(cols)

driver.quit()

df = pd.DataFrame(data, columns=["字", "注音", "拼音", "五行備註"])

df.to_excel('Strokes10.xlsx')
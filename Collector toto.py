from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import timedelta, date
import xlsxwriter



workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2021, 11, 11)
end_date = date(2021, 11, 19)
row=0
for single_date in daterange(start_date, end_date):
    #print("https://sg.gidapp.com/lottery/sp/toto/en/"+single_date.strftime("%Y-%m-%d"))
    driver = webdriver.Chrome(r"C:\Users\vishw\OneDrive\Documents\Python Scripts\Resources\chromedriver")
    #print("&&&&&&&&&&&&&&&&&&&&&")
    driver.get("https://sg.gidapp.com/lottery/sp/toto/en/"+single_date.strftime("%Y-%m-%d"))
    content = driver.page_source
    soup = BeautifulSoup(content)
    #for a in soup.findAll('a',href=True, attrs={'class':'table lotto g2'}):
    table = soup.find("table", attrs={"class": "table lotto g2"})
    if(table!=None):
        draw=[]
        draw.append(single_date.strftime("%Y-%m-%d"))
        draw.append("https://sg.gidapp.com/lottery/sp/toto/en/"+single_date.strftime("%Y-%m-%d"))
        #print(type(table))
        numbers_table = table.tbody.findAll("tr")
        #print(type(numbers_table))
        numbers=numbers_table[0]
        #print(numbers)
        #regex = re.compile('<span class="">(.*?)\</span>', re.IGNORECASE|re.DOTALL)
        #print(type(numbers))
        text=numbers.findAll("span")
        #print(text)
        #print(type(text))
        for k in text:
            draw.append(int(k.text))
        for col_num, data in enumerate(draw):
            worksheet.write(row, col_num, data)
        row=row+1
        print(draw)
    else:
        print("None")

    driver.quit();


workbook.close()









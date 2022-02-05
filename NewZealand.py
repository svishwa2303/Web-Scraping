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
#months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
months = ["december"]
#print(months)
for year in range(1995, 1996):
    for month in months:
        #print("http://lottoresults.co.nz/lotto/"+month+"-"+str(year))
        #print("https://sg.gidapp.com/lottery/sp/toto/en/"+single_date.strftime("%Y-%m-%d"))
        driver = webdriver.Chrome(r"C:\Users\vishw\OneDrive\Documents\Python Scripts\Resources\chromedriver")
        #print("&&&&&&&&&&&&&&&&&&&&&")
        driver.get("http://lottoresults.co.nz/lotto/"+month+"-"+str(year))       # http://lottoresults.co.nz/lotto/
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        #for a in soup.findAll('a',href=True, attrs={'class':'table lotto g2'}):
        table = soup.findAll("ol", attrs={"class": "draw-result"})
        #table[0]+=", <ol class=\"draw-result draw-result--sub\">"
        #print(table)
        #print(type(table))
        #print(type(table[0]))
        #print(soup)
        #print(soup.li)
        #print(type(soup.get_text()))
        if(table!=None):
            dates = []
            for link in soup.find_all('a'):
                if((month+"-"+str(year)) in link.get('href')):
                    dates.append(link.get('href').replace("/lotto/",""))
            #print(dates)
            datesIndex = 0
            #print(table)
            incrementer = 1
            list1 = iter(table)
            while(1):
                val = next(list1, 'length')
                if(val == 'length'):
                    break
                else:
                    draw=[]
                    draw.append(dates[datesIndex])
                    draw.append("http://lottoresults.co.nz/lotto/"+month+"-"+str(year))
                    values = val.getText()
                    #print(values)
                    values1 = values.split()
                    print(values.split())
                    datesIndex+=1
                    for k in values1:
                        draw.append(int(k))
                    storevalue = next(list1)
                    values = storevalue.getText()
                    values1 = values.split()
                    print(len(values1))
                    if(len(values1)==1):
                        values = next(list1).getText()
                        values1 = values.split()
                        print(values.split())
                        for k in values1:
                            draw.append(int(k))
                        values = storevalue.getText()
                        values1 = values.split()
                        for k in values1:
                            draw.append(int(k))
                    else:
                        for k in values1:
                            draw.append(int(k))
                    #print(type(table[value].getText()))
                    #print(resultTable)
                    #print(type(value))
                    for col_num, data in enumerate(draw):
                        worksheet.write(row, col_num, data)
                    row=row+1
                    print(draw)
            '''for value in range(0,len(table),1):
                incrementer = 1
                draw=[]
                draw.append(dates[datesIndex])
                draw.append("http://lottoresults.co.nz/lotto/"+month+"-"+str(year))
                #resultTable = value.find_all('ol')
                #print("***")
                #print(table[value])
                #print(table[value+1])
                values = table[value].getText()
                #print(values)
                values1 = values.split()
                print(values.split())
                datesIndex+=1
                for k in values1:
                    draw.append(int(k))
                values = table[value+1].getText()
                values1 = values.split()
                print(len(values1))
                if(len(values1)==4):
                    pass
                else:
                    values = table[value+2].getText()
                    values1 = values.split()
                    incrementer = 3
                print(values.split())
                for k in values1:
                    draw.append(int(k))
                #print(type(table[value].getText()))
                #print(resultTable)
                #print(type(value))
                for col_num, data in enumerate(draw):
                    worksheet.write(row, col_num, data)
                row=row+1
                print(draw)'''
        else:
            print("None")
    '''if(table!=None):
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
        print("None")'''

    driver.quit()


print("After pinting")
workbook.close()









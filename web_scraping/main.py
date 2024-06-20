from cgitb import text
import datetime
import requests
from bs4 import BeautifulSoup
from sqlalchemy import true
import time
import csv
import send_mail
from datetime import date
# url = "https://www.abaybanksc.com/saving-and-investments/"
urls=["https://finance.yahoo.com/quote/GOOG/","https://finance.yahoo.com/quote/AMZN/","https://finance.yahoo.com/quote/MSFT/"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
today = str(datetime.date.today()) + '.csv'
"""Write into csv files"""
csv_file = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Nme','Current Price','Previous Close','Open','Bid','Ask','Day Range','52 week Range','Volume','Avg. Value'])
for url in urls:
        stock =[]
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')  # Explicitly specify 'lxml' parser
            paragragh=soup.find_all("p")
            # for p in paragragh:
            #     text= p.get_text(strip=true)
            #     print(text)
            stock_title = soup.find("h1", class_="svelte-3a2v0c").get_text()
            current_price = soup.find_all("div",class_="container svelte-mgkamr")[0].find('span').get_text()
            stock.append(stock_title)
            stock.append(current_price)
            # print(soup.find('div'))
            table_info = soup.find_all("div",class_="container svelte-tx3nkj")[0].find_all("li")
            for i in range(8):
                    value =table_info[i].find_all("span")[1].get_text()
                    stock.append(value)
            csv_writer.writerow(stock)
            time.sleep(5)

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
csv_file.close()
send_mail.send(filename=today)
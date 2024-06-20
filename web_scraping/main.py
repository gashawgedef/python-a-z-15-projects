from cgitb import text
import requests
from bs4 import BeautifulSoup
from sqlalchemy import true

# url = "https://www.abaybanksc.com/saving-and-investments/"
url="https://finance.yahoo.com/quote/GOOG/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')  # Explicitly specify 'lxml' parser
    paragragh=soup.find_all("p")
    # for p in paragragh:
    #     text= p.get_text(strip=true)
    #     print(text)
    stock_title = soup.find("h1", class_="svelte-3a2v0c")
    print(stock_title.get_text())
    current_price = soup.find_all("div",class_="container svelte-mgkamr")[0].find('span').get_text()
    print(current_price)
    # print(soup.find('div'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

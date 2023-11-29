from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = "https://www.bloomberght.com/altin"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

rows = soup.find("div", {"class":"box box-12"}).find("tbody").find_all("tr")

gold_prices=[]
for row in rows:
    title = row.find("span").text
    price = row.find_all("td")[1].text
    list_row = [title, price]
    gold_prices.append(list_row)

header = ["Key", "Value"]
gold_df = pd.DataFrame(gold_prices, columns=header)
gold_df.to_csv("gold_prices.csv", index=False, sep=";")
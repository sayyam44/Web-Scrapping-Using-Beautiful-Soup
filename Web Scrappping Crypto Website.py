#scrapping the cryptocurrency name its price in a dictionary
from bs4 import BeautifulSoup
import requests
url="https://coinmarketcap.com/"
result = requests.get(url)
doc= BeautifulSoup(result.text,"html.parser")

tbody = doc.tbody
trs=tbody.contents
prices = {}
for tr in trs[:10]: #as we just want 1st 10 crypto
    name,price=tr.contents[2:4]
    fixed_name=name.p.string #as name was in the p tag in html 
    fixed_price = price.a.string #as price in the a tag in html file

    prices[fixed_name]=fixed_price
print(prices)
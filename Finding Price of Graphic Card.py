#Using Web Scrapping finding the price of the graphic card on website
from bs4 import BeautifulSoup
import requests
url="https://www.newegg.ca/asus-geforce-rtx-3060-dual-rtx3060-o12g-v2/p/N82E16814126524?Item=N82E16814126524"

result = requests.get(url)
doc= BeautifulSoup(result.text,"html.parser")
# print(doc.prettify())

prices=doc.find_all(text="$")
parent=prices[0].parent
strong=parent.find("strong")
print(strong.string)
# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f,"html.parser")

# print(doc.prettify())
# print(doc.title.string)
# tag=doc.title
# tag.string="Changed Title" #this changes the title of the html file

# print(doc)

# tags=doc.find_all("p")
# print(tags)
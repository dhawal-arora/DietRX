import requests
from bs4 import BeautifulSoup as soup
from nutrition_scraper import get_nutrition
import json

URL = "http://menuportal23.dining.rutgers.edu/FoodPro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=03&locationName=Livingston+Dining+Commons&naFlag=1"

req = requests.get(URL)

bs = soup(req.content, 'html5lib')
# print(bs.prettify())

breakfast = {}
lunch = {}
dinner = {}

form = bs.find('div', attrs={'class': 'menuBox'})

for name, nutrition in zip(form.find_all('div', attrs={'class': 'col-1'}), form.find_all('div', attrs={'class': 'col-3'})):
    # print(name.text)

    # breakfast[name.text]
    nutri_link = nutrition.a['href']
    # res = get_nutrition(nutri_link)
    nutri_link = 'http://menuportal23.dining.rutgers.edu/FoodPro/'+nutri_link
    # print(nutri_link)
    try:
        res = get_nutrition(nutri_link)
        # print(res)
        breakfast[name.get_text(strip=True)] = res
    except:
        print(f'did not get info on: {name.get_text(strip=True)}')

# print(breakfast)

w = open("breakfast.json", "w")
json = json.dumps(breakfast)
w.write(json)
w.close()

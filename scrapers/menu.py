import json
import requests
from bs4 import BeautifulSoup as soup
from scrapers.nutrition import get_nutrition

BASE_URL = "http://menuportal23.dining.rutgers.edu/FoodPro"


def scrape_menu(url):
    req = requests.get(url)
    bs = soup(req.content, 'html5lib')
    menu = {}
    form = bs.find('div', attrs={'class': 'menuBox'})

    for name, nutrition in zip(
        form.find_all('div', attrs={'class': 'col-1'}),
        form.find_all('div', attrs={'class': 'col-3'})
    ):
        nutri_link = f"{BASE_URL}/{nutrition.a['href']}"
        try:
            menu[name.get_text(strip=True)] = get_nutrition(nutri_link)
        except Exception:
            print(f"did not get info on: {name.get_text(strip=True)}")

    return menu


if __name__ == "__main__":
    LIVINGSTON_URL = (
        f"{BASE_URL}/pickmenu.asp?sName=Rutgers+University+Dining"
        "&locationNum=03&locationName=Livingston+Dining+Commons&naFlag=1"
    )
    breakfast = scrape_menu(LIVINGSTON_URL)
    with open("breakfast.json", "w") as f:
        f.write(json.dumps(breakfast))

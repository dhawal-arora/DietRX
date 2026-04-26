import requests
from bs4 import BeautifulSoup as soup


def get_nutrition(url):
    req = requests.get(url)
    bs = soup(req.content, 'html5lib')

    nutri_data_list = []
    table = bs.find('div', attrs={'id': 'nutritional-info'})
    specs = table.find('div', attrs={'id': 'specs'})
    tr = specs.find_all('tr')

    for i, nutri in enumerate(tr):
        if i == 0:
            continue
        for td in nutri.find_all('td'):
            nutri_data_list.append(td.get_text(strip=True))

    return nutri_data_list

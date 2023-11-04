import requests
from bs4 import BeautifulSoup as soup

# URL = "http://menuportal23.dining.rutgers.edu/foodpro/label.asp?RecNumAndPort=130019%2A1"

# req = requests.get(URL)

# bs = soup(req.content, 'html5lib')
# # print(bs.prettify())

# nutrition = {}

# table = bs.find('div', attrs={'id': 'nutritional-info'})
# # facts = bs.find('div', attrs={'id': 'facts'})
# # facs = {}
# # # facts['h2'] = form.h2.text
# # facs['p1'] = facts.p.text
# # facs['p2'] = facts.find_all_next('p')
# # print(facs['p2'])
# specs = table.find('div', attrs={'id': 'specs'})
# tr = specs.find_all('tr')

# line = []
# for i, nutri in enumerate(tr):
#     if i == 0:
#         continue
#     # print(nutri)
#     for j, td in enumerate(nutri.find_all('td')):
#         # if j == 1:
#         #     continue
#         # line[td.unwrap()] = td.text
#         # td.b.unwrap()
#         # print(td.get_text(strip=True))
#         line.append(td.get_text(strip=True))
#         # print((i, j))

# # nutrition[URL] = line

# print(line)


def get_nutrition(url):
    URL = url

    req = requests.get(URL)

    bs = soup(req.content, 'html5lib')
    # print(bs.prettify())

    nutri_data_list = []

    table = bs.find('div', attrs={'id': 'nutritional-info'})
    # facts = bs.find('div', attrs={'id': 'facts'})
    # facs = {}
    # # facts['h2'] = form.h2.text
    # facs['p1'] = facts.p.text
    # facs['p2'] = facts.find_all_next('p')
    # print(facs['p2'])
    specs = table.find('div', attrs={'id': 'specs'})
    tr = specs.find_all('tr')

    for i, nutri in enumerate(tr):
        if i == 0:
            continue
        # print(nutri)
        for j, td in enumerate(nutri.find_all('td')):
            # if j == 1:
            #     continue
            # line[td.unwrap()] = td.text
            # td.b.unwrap()
            # print(td.get_text(strip=True))
            nutri_data_list.append(td.get_text(strip=True))
            # print((i, j))

    # nutrition[URL] = line

    return nutri_data_list


# res = get_nutrition(
#     'http://menuportal23.dining.rutgers.edu/FoodPro/label.asp?RecNumAndPort=500512%2A1')
# print(res)

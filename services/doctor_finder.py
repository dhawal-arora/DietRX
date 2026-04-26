import requests
from bs4 import BeautifulSoup as soup
from database import cursor


def get_docs(user_id):
    cursor.execute(f"SELECT health FROM menu WHERE id={user_id};")
    condition = cursor.fetchone()[0]

    url = (
        "https://umg.rwjms.rutgers.edu/search_results.php"
        "?chosen_insurance=&chosen_insurance_label=&chosen_specialty="
        f"&chosen_symptoms_or_condition={condition}"
        "&typed_specialty=&typed_symptoms_or_condition=&view="
    )

    req = requests.get(url).text
    bs = soup(req, 'html5lib')

    body = bs.find('body')
    div1 = body.find('div', attrs={'id': 'container '})
    div2 = div1.find('div', attrs={'id': 'main-slide'})
    cont = div2.find('div', attrs={'class': 'container'})
    form = cont.find('form', attrs={'id': 'doc_form'})
    table_div = form.find('table', attrs={'class': 'table table-striped'})
    tbody = table_div.find('tbody')

    docs = {}
    for row in tbody.find_all('tr'):
        name = row.find('td').text
        cols = []
        for w, col in enumerate(row.find_all('td')):
            if w == 0:
                continue
            cols.append(col.get_text(strip=True))
        docs[name] = cols

    doctors = " "
    for a, name in enumerate(docs.keys()):
        doctors = doctors + str(name) + '\n' + str(docs[name][1]) + '\n' + str(docs[name][2]) + '\n\n'
        if a > 3:
            break

    return doctors

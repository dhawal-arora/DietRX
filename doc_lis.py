import requests
from bs4 import BeautifulSoup as soup
import mysql.connector as sqltor


def get_docs(id):
    mycon = sqltor.connect(host="na05-sql.pebblehost.com", user="customer_586593_ruontime",
                           passwd="TmzuYi1sOBxJ!qdy9d7j", database="customer_586593_ruontime")
    if mycon.is_connected():
        print('Succesfully Connected to MySql')
    cursor = mycon.cursor()
    command = "SELECT health FROM menu WHERE id="+str(id)+";"
    cursor.execute(command)
    print(command)
    condition = cursor.fetchone()
    print(condition)
    condition = condition[0]
    # discordtoken = "MTE3MDQwNzUzOTQwMjM1NDgwMA.GMTV-Y.6BAtXH8KoLmQIKW_nPmjnfxzJ-YKt5VaJ3JUzU"

    # URL = "https://www.zocdoc.com/search?address=08901&after_5pm=false&before_10am=false&day_filter=AnyDay&dr_specialty=153&filters=%7B%7D&fit_questionnaire_type=PCP&gender=-1&insurance_carrier=323&insurance_plan=2364&language=-1&offset=0&reason_visit=3849&searchOriginator=SearchBar&searchQueryGuid=&searchType=specialty&search_query=Primary+Care+Physician+%28PCP%29&sees_children=false&sort_type=Default&visitType=inPersonAndVirtualVisits"
    # URL = "https://umg.rwjms.rutgers.edu/find_provider.php"
    URL = "https://umg.rwjms.rutgers.edu/search_results.php?chosen_insurance=&chosen_insurance_label=&chosen_specialty=&chosen_symptoms_or_condition=" + \
        str(condition)+"&typed_specialty=&typed_symptoms_or_condition=&view="

    docs = {}

    req = requests.get(URL).text

    bs = soup(req, 'html5lib')

    body = bs.find('body')

    div1 = body.find('div', attrs={'id': 'container '})

    div2 = div1.find('div', attrs={'id': 'main-slide'})

    cont = div2.find('div', attrs={'class': 'container'})

    form = cont.find('form', attrs={'id': 'doc_form'})

    table_div = form.find('table', attrs={'class': 'table table-striped'})

    # table = table_div.find('table', attrs={'id': 'myTable'})
    tbody = table_div.find('tbody')

    for i in tbody.find_all('tr'):
        # docs[i.find('td').text]
        print(i.find('td').text)
        li = []
        for w, j in enumerate(i.find_all('td')):
            if w == 0:
                continue
            li.append(j.get_text(strip=True))

        docs[i.find('td').text] = li

    str = ""
    for a, q in enumerate(docs.keys()):
        str.append(q)
        str.append('\t')
        str.append(docs[q])
        if a > 1:
            break

    return str
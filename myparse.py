from bs4 import BeautifulSoup
import requests, codecs

def parse():
    url = 'https://omgtu.ru/ecab/persons/index.php?b=9'
    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")

    mainInfo = soup.findAll('div', class_='person__name')
    description = ''
    for data in mainInfo:
        if data.find('a'):
            description = description + data.text

    file = codecs.open('employees.txt', 'w', 'utf-8')
    file.write(description)
    file.close()
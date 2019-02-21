from contextlib import closing

from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def czy_poprawna_odp(odpowiedz):
    zawartosc = odpowiedz.headers['Content-Type'].lower()
    return (odpowiedz.status_code == 200 and
            zawartosc is not None and
            zawartosc.find('html') > -1)


def otworz_url(url):
    try:
        with closing(get(url, stream=True)) as odpowiedz:
            if czy_poprawna_odp(odpowiedz):
                return odpowiedz.content
            else:
                return None
    except RequestException as err:
        print(err)
        print("Prawdopodobnie nie odpowiedni link")


strumien = otworz_url('https://coinmarketcap.com/historical/20170220/')

html = BeautifulSoup(strumien, 'html.parser')

for i, li in enumerate(html.select('td')):
    if i == 4:
        print(li.text)

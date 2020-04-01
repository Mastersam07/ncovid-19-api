from bs4 import BeautifulSoup
import requests
import lxml.html as lh
import pandas as pd

url = "https://futa.edu.ng/"
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36',
    }
response = requests.get("https://covid19.ncdc.gov.ng", headers=headers)
content = BeautifulSoup(response.content, "html.parser")

print(content.prettify())

tb = content.find('table', id_='custom3')

for link in tb.find_all('b'):
    name = link.find('a')
    print(name)

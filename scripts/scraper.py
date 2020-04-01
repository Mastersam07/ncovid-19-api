from bs4 import BeautifulSoup
import requests
import numpy as np


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua


url = "https://futa.edu.ng/"
user_agent = get_random_ua()
headers = {
    'user-agent': user_agent,
}
r = requests.get('https://covid19.ncdc.gov.ng', headers=headers)

# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/56.0.2924.87 Safari/537.36',
# }
content = BeautifulSoup(r.content, "html.parser")

print(content.prettify())

# tb = content.find('table', id_='custom3')
# #
# # for link in tb.find_all('b'):
# #     name = link.find('a')
# #     print(name)


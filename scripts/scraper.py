from bs4 import BeautifulSoup
import requests

# import numpy as np
import pandas as pd

# delays = [12, 3, 9, 21, 5, 6, 19, 7, 33, 11, 2, 17, 4]
#
#
# def get_random_ua():
#     random_ua = ''
#     ua_file = 'ua_file.txt'
#     try:
#         with open(ua_file) as f:
#             lines = f.readlines()
#         if len(lines) > 0:
#             while not random_ua.strip():
#                 prng = np.random.RandomState()
#                 index = prng.permutation(len(lines) - 1)
#                 idx = np.asarray(index, dtype=np.integer)[0]
#                 random_proxy = lines[int(idx)]
#     except Exception as ex:
#         print('Exception in random_ua')
#         print(str(ex))
#     finally:
#         return random_ua
#
#
# url = "https://futa.edu.ng/"
# user_agent = get_random_ua()
headers = {
    #     # 'user-agent': user_agent,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
    #     'referer': 'https://google.ng/',
    #     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     # 'Accept-Encoding': 'gzip, deflate, br',
    #     # 'Accept-Language': 'en-US,en;q=0.9',
    #     # 'Pragma': 'no-cache',
}
r = requests.get('https://covid19.ncdc.gov.ng', headers=headers, timeout=5)
print(r.status_code)

content = BeautifulSoup(r.text, 'lxml')
# print(r.status_code)

# print(content.prettify())

My_table = content.find('table', {'id': 'custom3'})
# print(My_table)
links = My_table.findAll('b')
stately = My_table.findAll('td')

data = []
for link in links:
    data.append(link)
states = []
for state in stately:
    states.append(state)

some = []

for i in range(0, len(states), 2):
    some.append(states[i])

df = pd.DataFrame()
df['states'] = some
df['Cases'] = data
print(df)
# df.to_sql(r'C:\Users\USER\Desktop\Flutter\Challenge\ncovid-19-api\api\ncovid.sql', index=False)
# print("SUCCESS!!!")

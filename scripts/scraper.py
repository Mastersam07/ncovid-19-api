import csv

from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine  # db engine
import pandas as pd

"""
delays = [12, 3, 9, 21, 5, 6, 19, 7, 33, 11, 2, 17, 4]


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            while not random_ua.strip():
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

"""
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

# make a request with headers
r = requests.get('https://covid19.ncdc.gov.ng', headers=headers, timeout=5)

print(r.status_code)  # 200 for success

content = BeautifulSoup(r.text, 'lxml')  # parsing content

My_table = content.find('table', {'id': 'custom3'})  # table to be scrapped having id as custom3

links = My_table.findAll('b')  # all cases data seems to be in b tags
stately = My_table.findAll('td')  # all state name seems to be in td tags

# print(links)

# save cases data to list
cases = []
for link in links:
    cases.append(link.text)

# save states data to list
states = []
for state in stately:
    states.append(state.text)

# escape string appears in list in odd indexes
# get states with even indexes
somes = []
for i in range(0, len(states), 2):
    somes.append(states[i])

# take data to pandas dataframe
df = pd.DataFrame()
df['States'] = somes
df['Cases'] = cases

print('Dataframe\n', df)

# save data to csv
df.to_csv(r'ncovid.csv', index=True, index_label='id')
print("SUCCESS!!!")

# import sqlite3
# #
# conn = sqlite3.connect(r"C:\Users\USER\Desktop\Flutter\Challenge\ncovid-19-api\api\db.sqlite3")
# cur = conn.cursor()
# cur.execute("CREATE TABLE data (id NOT_NULL AUTO_INCREMENT,States, Cases);")
# sql = "INSERT INTO data(States, Cases) VALUES (df.States, df.Cases);"
# cur.execute(sql)
# conn.commit()
# cur.execute("select * from data;")
# results = cur.fetchall()
# print(results)
#
# # engine = create_engine(r'sqlite:///C:\Users\USER\Desktop\Flutter\Challenge\ncovid-19-api\api\db.sqlite3')
# # (df['States']).to_sql(name='states_stat', con=engine, if_exists='replace', index=False)
# # (df['Cases']).to_sql(name='states_cases', con=engine, if_exists='replace', index=False)
# #
# # print('Data transferred from df to sqlite!!!')
# #
# # print('Checking the data...')
#
# # import sqlite3
# #
# # conn = sqlite3.connect(r"C:\Users\USER\Desktop\Flutter\Challenge\ncovid-19-api\api\db.sqlite3")
# # cur = conn.cursor()
# # cur.execute("CREATE TABLE data (States, Cases);")
# # with open('ncovid.csv', 'rb') as fin:  # `with` statement available in 2.5+
# #     # csv.DictReader uses first line in file for column headings by default
# #     dr = csv.DictReader(fin)  # comma is default delimiter
# #     to_db = [(i['States'], i['Cases']) for i in dr]
# #
# # cur.executemany("INSERT INTO data (States, Cases) VALUES (?, ?);", to_db)
# # conn.commit()
# # conn.close()
# # cur.execute("select * from data;")
# # results = cur.fetchall()
# # print(results)

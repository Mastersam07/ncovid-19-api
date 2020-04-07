import sqlite3

import psycopg2
from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine  # db engine
import pandas as pd

headers = {
    #     # 'user-agent': user_agent,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
}

# make a request with headers
r = requests.get('https://covid19.ncdc.gov.ng', headers=headers, timeout=15)

print(r.status_code)  # 200 for success

content = BeautifulSoup(r.text, 'lxml')  # parsing content

My_table = content.find('table', {'id': 'custom1'})  # table to be scrapped having id as custom3

links = My_table.findAll('b')  # all cases data seems to be in b tags
stately = My_table.findAll('td')  # all state name seems to be in td tags

# save cases data to list
cases = []
for link in links:
    cases.append(link.text)
#
# save states data to list
states = []
for state in stately:
    states.append(state.text)

# escape string appears in list in odd indexes
# get states with even indexes
somes = []
for i in range(0, len(states), 2):
    somes.append(states[i])

print(cases)
print(somes)

# take data to pandas dataframe
df = pd.DataFrame()
df['Categories'] = somes
df['Values'] = cases

print('Dataframe\n', df)

# save data to csv
# df.to_csv(r'ncovid.csv', index=True, index_label='id')
# print("SUCCESS!!!")
#
# from sqlalchemy import create_engine

# sqlite engine
# engine = create_engine(r'sqlite:///db.sqlite3')

# connections for sqlite
# con = sqlite3.connect(r"C:\Users\USER\Desktop\ncovid-19-api\api\db.sqlite3")

# connections for postgresql
# con = psycopg2.connect(host="localhost", database="ncovid", user="postgres", password="mastersam")

# add postgres db engine
engine = create_engine('postgresql+psycopg2://postgres:mastersam@localhost/ncovid')
#
# adding df to tables
df.to_sql(con=engine, name='confirmed', if_exists='replace', index=True, index_label='id')
#
print('Data transferred from df to postgresql successfully!!!')

# checking the data
print('checking the data...')
conn = psycopg2.connect(host="localhost", database="ncovid", user="postgres", password="mastersam")
cur = conn.cursor()
cur.execute("SELECT * FROM confirmed")

rows = cur.fetchall()

for row in rows:
    print(row)
print('Done checking!!!')

conn.close()

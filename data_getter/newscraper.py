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

# print(r.status_code)  # 200 for success

content = BeautifulSoup(r.text, 'lxml')  # parsing content

My_table = content.findAll('div', {'class': 'col-xs-3 col-md-3 col-xl-3'})  # div for all data
Samples = content.find('div', {'class': 'col-md-12 col-xl-3'})  # div for total tested sapmles

# print(Samples.find('span').text)
# assign each div
confirmed_cases = My_table[0]
active_cases = My_table[1]
discharged_cases = My_table[2]
death = My_table[3]

# get the category data
sample_cat = Samples.find('h6').text
confirmed_cat = confirmed_cases.find('h6').text
active_cat = active_cases.find('h6').text
discharged_cat = discharged_cases.find('h6').text
death_cat = death.find('h6').text

# get the figures data
sample_data = Samples.find('span').text
confirmed_data = confirmed_cases.find('h2').text
active_data = active_cases.find('h2').text
discharged_data = discharged_cases.find('h2').text
death_data = death.find('h2').text

# check data
print(sample_cat, sample_data)
print(confirmed_cat, confirmed_data)
print(active_cat, active_data)
print(discharged_cat, discharged_data)
print(death_cat, death_data)

# pass all outputs to list
somes = [sample_cat, confirmed_cat, discharged_cat, death_cat]
cases = [sample_data, confirmed_data, discharged_data, death_data]

# print(cases)
# print(somes)

# take data to pandas dataframe
df = pd.DataFrame()
df['Categories'] = somes
df['Values'] = cases

print('Dataframe\n', df)

# save data to csv
# df.to_csv(r'ncovid.csv', index=True, index_label='id')
# print("SUCCESS!!!")

# add postgres db engine
engine = create_engine('postgresql+psycopg2://postgres:mastersam@localhost/ncovid')
#
# adding df to tables
df.to_sql(con=engine, name='confirmed', if_exists='replace', index=True, index_label='id')
#
print('Data transferred from df to postgresql successfully!!!')
#
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

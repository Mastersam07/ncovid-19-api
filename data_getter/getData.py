#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import locale

# use local to convert comma formatted string numbers into Python integers
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def update_database():
    headers = {
        #     # 'user-agent': user_agent,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36',
    }
    url = 'https://covid19.ncdc.gov.ng'

    # make a request with headers
    r = requests.get(url, headers=headers, timeout=5)

    print(r.status_code)  # 200 for success

    content = BeautifulSoup(r.text, 'lxml')  # parsing content

    # table to be scrapped having id as custom1
    My_table = content.find('table', {'id': 'custom1'})

    # scrape the whole table. including state names and cases data
    data = My_table.findAll('td')

    # save states data to a list
    states = [data[index].text.strip() for index in range(0, len(data), 5)]
    # save number of confirmed cases data to a list
    cases = [locale.atoi(data[index].text.strip())
             for index in range(1, len(data), 5)]
    # save number of admissions to a list
    admissions = [locale.atoi(data[index].text.strip())
                  for index in range(2, len(data), 5)]
    # save number of recovered cases data to a list
    dischared = [locale.atoi(data[index].text.strip())
                 for index in range(3, len(data), 5)]
    # save number of deaths to a list
    deaths = [locale.atoi(data[index].text.strip())
              for index in range(4, len(data), 5)]


    # take data to pandas dataframe
    df = pd.DataFrame()
    df['States'] = states
    df['No_of_cases'] = cases
    df['No_on_admission'] = admissions
    df['No_discharged'] = dischared
    df['No_of_deaths'] = deaths

    print('Dataframe\n', df)

    # save data to csv
    df.to_csv(r'ncovid.csv', index=True, index_label='id')
    print("SUCCESS!!!")

    # create sqlite engine
    # engine = create_engine(r'db.sqlite3')

    # add postgres db engine
    engine = create_engine('postgresql+psycopg2://postgres:mastersam@localhost/ncovid')

    # adding df to tables
    df.to_sql(con=engine, name='data', if_exists='replace', index=True, index_label='id')

    print('Data transferred from df to postgres successfully!!!')


if __name__ == "__main__":
    update_database()

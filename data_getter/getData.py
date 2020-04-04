import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine


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

    My_table = content.find('table', {'id': 'custom3'})  # table to be scrapped having id as custom3

    links = My_table.findAll('b')  # all cases data seems to be in b tags
    stately = My_table.findAll('td')  # all state name seems to be in td tags

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

    # set length to be 37 due to irregularities

    # take data to pandas dataframe
    df = pd.DataFrame()
    df['States'] = somes[0:37]
    df['Cases'] = cases[0:37]

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

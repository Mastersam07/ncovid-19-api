import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df = pd.read_csv("daily_report.csv")

# add postgres db engine
engine = create_engine('postgresql+psycopg2://postgres:mastersam@localhost/ncovid')
#
# adding df to tables
df.to_sql(con=engine, name='daily', if_exists='replace', index=True, index_label='id')
#
print('Data transferred from df to postgresql successfully!!!')

# checking the data
print('checking the data...')
conn = psycopg2.connect(host="localhost", database="ncovid", user="postgres", password="mastersam")
cur = conn.cursor()
cur.execute("SELECT * FROM daily")

rows = cur.fetchall()

for row in rows:
    print(row)
print('Done checking!!!')

conn.close()

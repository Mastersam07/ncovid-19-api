from bs4 import BeautifulSoup
import requests
import pandas as pd


def reorder_states(text):
    for eachstate in text:
        df['States'] = text[5:-6]
    text.to_string()
    new_text = text[5:-6]
    return new_text


def reorder_cases(text):
    text.to_string()
    new_text = text[3:-4]
    return new_text


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

# save cases data to list
cases = []
for link in links:
    cases.append(link.iloc)

# save states data to list
states = []
for state in stately:
    states.append(state)

# escape string appears in list in odd indexes
# get states with even indexes
some = []
for i in range(0, len(states), 2):
    some.append(states[i])

# take data to pandas dataframe
df = pd.DataFrame()
df['States'] = some
df['Cases'] = cases

# # removing garbage from states
df['States'] = df['States'].to_string()

# removing garbage from cases
df['Cases'] = df['Cases'].to_string()

# print(type(df.dtypes))

# save data to csv
df.to_csv(r'C:\Users\USER\Desktop\Flutter\Challenge\ncovid-19-api\api\ncovid.csv', index=False)
print("SUCCESS!!!")

# tweet = content.findAll('p', attrs={"class": "content"}).text
# print tweet
#
# for tweet in content.findAll('p', attrs={"class": "content"}):
#     print tweet.text.encode('utf-8')

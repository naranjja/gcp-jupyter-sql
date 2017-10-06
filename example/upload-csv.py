import pandas as pd
from sqlalchemy import create_engine
from json import load

print('Loading settings...')
file = open('settings.json', 'r')
settings = load(file)
file.close()

print('Connecting to database...')
url = 'postgresql+psycopg2://{user}:{pass}@{host}:5432/{db}'.format(**settings)
engine = create_engine(url, client_encoding='utf8')

print('Reading CSV...')
df = pd.read_csv(settings['csv'])

print('Storing results...')
df.to_sql(settings['table'], con=engine, if_exists='replace')

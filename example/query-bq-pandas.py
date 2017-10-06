import pandas as pd
from json import load

print('Loading settings...')
file = open('settings.json', 'r')
settings = load(file)
file.close()

query = """
    SELECT *
    FROM {project_id}:{dataset}.{table}
""".format(**settings)

print('Performing query...')
df = pd.read_gbq(query, project_id=settings['project_id'])
print(df)

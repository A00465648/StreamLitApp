import matplotlib.pyplot as plt
import pandas as pd
import requests

url = 'https://data.nasdaq.com/api/v3/datasets/WIKI/GOOGL.json'
api_key = "6GBbY5Dak2r8t36CSbXs"
r_data = requests.get(url, params=dict(api_key=api_key), ).json()
df = pd.DataFrame(r_data['dataset']['data'], columns=r_data['dataset']['column_names'])
df.sort_values(by="Date", inplace=True)
# print(r_data_df)
df.plot("Date", "Open", kind="line")
plt.show()

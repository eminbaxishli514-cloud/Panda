import pandas as pd
import requests
url="https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response =requests.get(url, headers=headers)
tables=pd.read_html(response.text)
print(tables[3].groupby("NOC").agg({'Gold':'sum','Silver':'sum','Bronze':'sum','Total':'sum'}))
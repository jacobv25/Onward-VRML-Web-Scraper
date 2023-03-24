import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://vrmasterleague.com/Onward/Teams/3VgXYBAGsQaGFmkhNp3bTA2"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

table = soup.find("table", {"class": "teams_stats_maps_current_season_table vrml_table"})

headers = []
for th in table.find_all("th"):
    headers.append(th.text.strip())

data = []
for tr in table.find_all("tr"):
    row = []
    for td in tr.find_all("td"):
        row.append(td.text.strip())
    if row:
        data.append(row)

df = pd.DataFrame(data, columns=headers)

print(df)
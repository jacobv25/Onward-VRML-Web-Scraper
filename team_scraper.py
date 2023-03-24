import requests
from bs4 import BeautifulSoup
import pandas as pd

class TeamScraper:
    def __init__(self, team_id):
        self.base_url = f"https://vrmasterleague.com{team_id}"
        self.team_id = team_id

    def fetch_content(self, url):
        response = requests.get(url)
        content = response.content
        return BeautifulSoup(content, "html.parser")

    def get_season_values(self, soup):
        season_select = soup.find("select", {"class": "team_season_switcher"})
        season_values = [option["value"] for option in season_select.find_all("option")]
        return season_values[-4:]

    def extract_table_data(self, soup):
        table = soup.find("table", {"class": "teams_stats_maps_current_season_table vrml_table"})
        headers = [th.text.strip() for th in table.find_all("th")]

        data = []
        for tr in table.find_all("tr"):
            row = [td.text.strip() for td in tr.find_all("td")]
            if row:
                data.append(row)

        return headers, data

    def scrape_team_data(self):
        soup = self.fetch_content(self.base_url)
        season_values = self.get_season_values(soup)
        season_dfs = []

        for season_value in season_values:
            url = f"{self.base_url}?season={season_value}"
            soup = self.fetch_content(url)
            headers, data = self.extract_table_data(soup)

            for row in data:
                row.append(season_value)

            df = pd.DataFrame(data, columns=headers+["Season"])
            season_dfs.append(df)

        team_df = pd.concat(season_dfs, ignore_index=True)
        return team_df

    @staticmethod
    def convert_season_value_to_number(df):
        seasons = df["Season"].unique()
        starting_season_number = max(14 - len(seasons) + 1, 1)
        season_numbers = list(range(starting_season_number, starting_season_number + len(seasons)))
        season_mapping = {seasons[i]: season_numbers[i] for i in range(len(seasons))}

        new_df = df.copy()
        new_df["Season"] = new_df["Season"].apply(lambda season: season_mapping[season])

        return new_df


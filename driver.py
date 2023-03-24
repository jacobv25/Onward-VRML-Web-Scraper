import requests
from bs4 import BeautifulSoup
import pandas as pd
from team_scraper import TeamScraper
from web_scraper import WebScraper

def main():
    # Scrape team links
    url = "https://vrmasterleague.com/Onward/Standings/"
    web_scraper = WebScraper(url)
    web_scraper.scrape()
    team_links = web_scraper.hrefs

    # Scrape data for each team and store in a list of DataFrames
    all_teams_data = []
    for team_link in team_links:
        team_id = team_link.split('/')[-1]
        team_scraper = TeamScraper(team_id)
        team_data = team_scraper.scrape_team_data()
        team_data = team_scraper.convert_season_value_to_number(team_data)
        
        print(team_data)
        
        all_teams_data.append(team_data)

    # Combine all DataFrames into a single DataFrame
    final_df = pd.concat(all_teams_data, ignore_index=True)
    print(final_df)

if __name__ == "__main__":
    main()
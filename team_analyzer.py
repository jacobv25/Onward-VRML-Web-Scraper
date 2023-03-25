import pandas as pd
from team_scraper import TeamScraper

class TeamAnalyzer:
    def __init__(self, team_id):
        self.team_id = team_id
        self.team_df = None

    def scrape_team_data(self):
        scraper = TeamScraper(self.team_id)
        self.team_df = scraper.scrape_team_data()
        self.team_df = scraper.convert_season_value_to_number(self.team_df)
        self.team_df['ROUNDS PLAYED'] = pd.to_numeric(self.team_df['ROUNDS PLAYED'])
        self.team_df['ROUNDS WIN'] = pd.to_numeric(self.team_df['ROUNDS WIN'])

    def get_win_percentages_by_map(self):
        rounds_played = self.team_df.groupby('MAP')['ROUNDS PLAYED'].sum()
        rounds_won = self.team_df.groupby('MAP')['ROUNDS WIN'].sum()
        win_percentages = (rounds_won / rounds_played) * 100
        return win_percentages.sort_values(ascending=False)

    def get_rounds_played_and_won_by_map(self):
        rounds_played = self.team_df.groupby('MAP')['ROUNDS PLAYED'].sum()
        rounds_won = self.team_df.groupby('MAP')['ROUNDS WIN'].sum()
        rounds_played = rounds_played.sort_values(ascending=False)
        rounds_won = rounds_won[rounds_played.index]
        return rounds_played, rounds_won

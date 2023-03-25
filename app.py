from flask import Flask, render_template, request, Markup
import pandas as pd
from team_scraper import TeamScraper
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        team_id = request.form.get("team_id")
        scraper = TeamScraper(team_id)
        team_df = scraper.scrape_team_data()
        team_df = scraper.convert_season_value_to_number(team_df)

        # Convert relevant columns to numeric types
        team_df['ROUNDS PLAYED'] = pd.to_numeric(team_df['ROUNDS PLAYED'])
        team_df['ROUNDS WIN'] = pd.to_numeric(team_df['ROUNDS WIN'])
        
        rounds_played = team_df.groupby('MAP')['ROUNDS PLAYED'].sum()
        rounds_won = team_df.groupby('MAP')['ROUNDS WIN'].sum()

        win_percentages = (rounds_won / rounds_played) * 100
        win_percentages = win_percentages.sort_values(ascending=False)

        fig = px.bar(win_percentages, x=win_percentages.index, y=win_percentages.values, text=win_percentages.values, title='Win Percentages by Map')
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(xaxis_title='Map', yaxis_title='Win Percentage', yaxis_tickformat='%')

        plot_html = pio.to_html(fig, full_html=False)

        return render_template('index.html', team_df=team_df.to_html(), plot_html=plot_html)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
from team_scraper import TeamScraper
import plotly.express as px

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

        # Create a bar chart of win percentages by map using Plotly
        fig_bar = px.bar(win_percentages, x=win_percentages.index, y=win_percentages.values, text=win_percentages.values,
                     title='Win Percentages by Map')
        fig_bar.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_bar.update_layout(xaxis_title='Map', yaxis_title='Win Percentage', yaxis_tickformat='%')

        # Create a scatter plot of win percentages vs. number of rounds played using Plotly
        fig_scatter = px.scatter(team_df, x='ROUNDS PLAYED', y='ROUNDS WIN', color='MAP', title='Win Percentage vs. Rounds Played')
        fig_scatter.update_traces(mode='markers', marker_size=10)

        # Generate the HTML code for the plots
        plot_html_bar = fig_bar.to_html(full_html=False)
        plot_html_scatter = fig_scatter.to_html(full_html=False)

        return render_template('index.html', team_df=team_df.to_html(), plot_html_bar=plot_html_bar, plot_html_scatter=plot_html_scatter)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

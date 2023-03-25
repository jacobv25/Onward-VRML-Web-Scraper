from flask import Flask, render_template, request
from team_analyzer import TeamAnalyzer
import plotly.express as px
import plotly.graph_objs as go

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        team_id = request.form.get("team_id")
        analyzer = TeamAnalyzer(team_id)
        analyzer.scrape_team_data()

        win_percentages = analyzer.get_win_percentages_by_map()

        # Create a bar chart of win percentages by map using Plotly
        fig_bar = px.bar(win_percentages, x=win_percentages.index, y=win_percentages.values, text=win_percentages.values,
                     title='Win Percentages by Map')
        fig_bar.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_bar.update_layout(xaxis_title='Map', yaxis_title='Win Percentage', yaxis_tickformat='%')

        # Create a scatter plot of win percentages vs. number of rounds played using Plotly
        rounds_played, rounds_won = analyzer.get_rounds_played_and_won_by_map()
        fig_scatter = px.scatter(analyzer.team_df, x='ROUNDS PLAYED', y='ROUNDS WIN', color='MAP', title='Win Percentage vs. Rounds Played')
        fig_scatter.update_traces(mode='markers', marker_size=10)

        # Generate the HTML code for the plots
        plot_html_bar = fig_bar.to_html(full_html=False)
        plot_html_scatter = fig_scatter.to_html(full_html=False)

        # Create a stacked bar chart of the rounds played and won on each map using Plotly
        fig_stacked = go.Figure(data=[
            go.Bar(name='Rounds Played', x=rounds_played.index, y=rounds_played.values),
            go.Bar(name='Rounds Won', x=rounds_won.index, y=rounds_won.values, marker_color='green')
        ])
        fig_stacked.update_layout(title='Rounds Played and Won by Map', xaxis_title='Map', yaxis_title='Number of Rounds')
        stacked_bar_html = fig_stacked.to_html(full_html=False)

        return render_template('index.html', team_df=analyzer.team_df.to_html(), plot_html_bar=plot_html_bar, plot_html_scatter=plot_html_scatter, stacked_bar=stacked_bar_html)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

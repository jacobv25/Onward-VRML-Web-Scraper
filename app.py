# app.py
from flask import Flask, request, render_template_string
import pandas as pd
from team_scraper import TeamScraper  # Assuming you have saved the TeamScraper class in a file named team_scraper.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        team_id = request.form.get("team_id")
        scraper = TeamScraper(team_id)
        team_df = scraper.scrape_team_data()
        team_df = scraper.convert_season_value_to_number(team_df)
        return team_df.to_html()
    return '''
    <form method="post">
        Team ID: <input type="text" name="team_id"><br>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

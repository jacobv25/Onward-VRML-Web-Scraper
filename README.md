Onward-VRML-Web-Scraper
This repository contains a Python web scraper for the Onward VR Master League website. It includes two primary scripts, team_scraper.py and web_scraper.py, as well as a Flask web app, app.py, that provides an interface for users to input a team ID and receive a DataFrame containing team data.

Installation
Clone this repository to your local machine.
Install required packages (preferably in a virtual environment) using the following command:
Copy code
pip install requests beautifulsoup4 pandas flask
Usage
TeamScraper (team_scraper.py)
This script contains the TeamScraper class, which allows you to scrape team data from the Onward VR Master League website by providing a team ID.

python
Copy code
from team_scraper import TeamScraper

team_id = "/Teams/TeamID"
scraper = TeamScraper(team_id)
team_df = scraper.scrape_team_data()
team_df = scraper.convert_season_value_to_number(team_df)
WebScraper (web_scraper.py)
This script contains the WebScraper class, which allows you to scrape team IDs from the Onward VR Master League website by providing a URL.

python
Copy code
from web_scraper import WebScraper

url = "https://vrmasterleague.com/Onward/Teams/"
web_scraper = WebScraper(url)
web_scraper.scrape()
team_ids = web_scraper.hrefs
Flask Web App (app.py)
The Flask web app allows users to input a team ID and receive a DataFrame containing team data.

To run the app, execute the following command in the terminal:

Copy code
python app.py
This will start a local server, and you can access the web app by visiting http://127.0.0.1:5000/ in your web browser.

Enter a team ID in the provided form, and click "Submit" to receive a DataFrame with the team's data.

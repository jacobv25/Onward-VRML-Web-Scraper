# Onward-VRML-Web-Scraper
This repository contains a Python web scraper for the Onward VR Master League website. It includes two primary scripts, team_scraper.py and web_scraper.py, as well as a Flask web app, app.py, that provides an interface for users to input a team ID and receive a DataFrame containing team data.

## Installation
1. Clone this repository to your local machine.
1. Install required packages (preferably in a virtual environment) using the following command:
```
pip install requests beautifulsoup4 pandas flask
```
## Usage
### TeamScraper (team_scraper.py)
This script contains the TeamScraper class, which allows you to scrape team data from the Onward VR Master League website by providing a team ID.

```
from team_scraper import TeamScraper

team_id = "/Teams/TeamID"
scraper = TeamScraper(team_id)
team_df = scraper.scrape_team_data()
team_df = scraper.convert_season_value_to_number(team_df)
```
### WebScraper (web_scraper.py)
This script contains the WebScraper class, which allows you to scrape team IDs from the Onward VR Master League website by providing a URL.
```
from web_scraper import WebScraper

url = "https://vrmasterleague.com/Onward/Teams/[random string of characters]"
web_scraper = WebScraper(url)
web_scraper.scrape()
team_ids = web_scraper.hrefs
```
### Flask Web App (app.py)
The Flask web app allows users to input a team ID and receive a DataFrame containing team data.

To run the app, execute the following command in the terminal:
```
python app.py
```
This will start a local server, and you can access the web app by visiting http://127.0.0.1:5000/ in your web browser.

Enter a team ID in the provided form, and click "Submit" to receive a DataFrame with the team's data.

### Team ID format
A team ID is a unique identifier that represents a specific team in the Onward VR Master League website. It has a specific format that follows the URL structure of the website.

The team ID format includes the game name, "Onward", the section "Teams", and a random string of characters that represents the team. The format looks like this:

```
/Onward/Teams/[random string of characters]
```
An example of a team ID is:

```
/Onward/Teams/nDQ9eqQEOiPOsAUgCrv-0A2
```
It's important to note that the random string of characters in the team ID is unique to each team and cannot be used to represent any other team in the league. Therefore, it's crucial to use the correct team ID to retrieve accurate team data using the Onward-VRML-Web-Scraper tool.

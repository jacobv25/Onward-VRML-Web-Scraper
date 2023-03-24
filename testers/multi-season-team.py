import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Define the base URL and team ID
base_url = "https://vrmasterleague.com/Onward/Teams/nDQ9eqQEOiPOsAUgCrv-0A2"
team_id = "nDQ9eqQEOiPOsAUgCrv-0A2"

# Fetch the content of the web page
response = requests.get(base_url)
content = response.content

# Create a BeautifulSoup object from the content
soup = BeautifulSoup(content, "html.parser")

# Find the select element containing the season options
season_select = soup.find("select", {"class": "team_season_switcher"})

# Extract the value attribute from each option element
season_values = [option["value"] for option in season_select.find_all("option")]

# Create an empty list to store the dataframes for each season
season_dfs = []

# Loop over the previous three seasons (assuming they exist)
for season_value in season_values:
        
    # Construct the URL for the season
    url = f"{base_url}?season={season_value}"
    
    # Fetch the content of the web page
    response = requests.get(url)
    content = response.content
    
    # Create a BeautifulSoup object from the content
    soup = BeautifulSoup(content, "html.parser")
    
    # Find the table you want to scrape using its class or other attributes
    table = soup.find("table", {"class": "teams_stats_maps_current_season_table vrml_table"})
    
    # Extract the table headers
    headers = []
    for th in table.find_all("th"):
        headers.append(th.text.strip())
    
    # Extract the table rows and cells
    data = []
    for tr in table.find_all("tr"):
        row = []
        for td in tr.find_all("td"):
            row.append(td.text.strip())
        if row:
            row.append(season_value)  # Add the season value to the row
            data.append(row)
    
    # Create a DataFrame from the headers and data
    df = pd.DataFrame(data, columns=headers+["Season"])
    
    # Append the DataFrame to the list of season DataFrames
    season_dfs.append(df)
    
# Concatenate the season DataFrames into a single DataFrame
team_df = pd.concat(season_dfs, ignore_index=True)

print(team_df)

def convert_season_value_to_number(df):
    """
    Convert the season values in a DataFrame to season numbers.

    Args:
        df (pandas.DataFrame): The DataFrame containing the season values.

    Returns:
        pandas.DataFrame: The DataFrame with the season values replaced with season numbers.
    """
    # seasons = sorted(set(df["Season"]), reverse=True)  # Get a sorted list of unique season values
    seasons = df["Season"].unique()  # Get a list unique season values

    season_numbers = list(range(7, len(seasons) + 7))  # Generate a list of season numbers
    
    # Create a dictionary mapping each season value to its corresponding season number
    season_mapping = {seasons[i]: season_numbers[i] for i in range(len(seasons))}
    
    # Create a new DataFrame with the season values replaced with season numbers
    new_df = df.copy()
    new_df["Season"] = new_df["Season"].apply(lambda season: season_mapping[season])
    
    return new_df

# Print the DataFrame
print(convert_season_value_to_number(team_df))

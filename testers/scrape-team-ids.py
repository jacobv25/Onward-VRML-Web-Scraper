import requests
from bs4 import BeautifulSoup

# Replace 'your_url' with the URL of the web page you want to scrape
url = 'https://vrmasterleague.com/Onward/Standings/NA'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with the class 'team_link'
team_link_elements = soup.find_all('a', class_='team_link')

# Loop through the elements and print the href attribute of each element
for team_link_element in team_link_elements:
    href = team_link_element['href']
    print(href)

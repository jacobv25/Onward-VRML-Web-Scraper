import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.hrefs = []

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        team_link_elements = soup.find_all('a', class_='team_link')
        self.hrefs = [element['href'] for element in team_link_elements]

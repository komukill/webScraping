"""
Scrape Hacker News site for its top 30 news.
Save scraped data (title & link to thread) as a time-stamped JSON file.
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime as dt

url = 'https://news.ycombinator.com'
response = requests.get(url)
response = BeautifulSoup(response.text, 'html.parser')
titles = response.findAll('a', class_='storylink')
newsList = {}

#top 30 news
for title in titles:
    news = {
        "news": title.get_text(),
        "link": title.get('href')
    }
    newsList[titles.index(title)+1] = news
    
with open("hackerNewsTop_{}.json".format(dt.now().strftime('%d-%m-%y_%H:%M:%S')), 'a') as file:
    json.dump(newsList, file, indent=4)
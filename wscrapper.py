import bs4 as BeautifulSoup4
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?x=154&y=72&site=mlb&zmx=&zmy=&map_x=154&map_y=72#.Xf35eRdKgqJ')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
#print(week)
items = week.find_all(class_='tombstone-container')
#print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text()for item in items]
short_descriptions = [item.find(class_='short-desc').get_text()for item in items]
print(period_names)
print(short_descriptions)


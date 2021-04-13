# Example of web scraping code

# Get query to the website, getting the html with the site's information, to then parsing the received data
# Important libraries:
# Beautiful Soup, lxml, requests
import requests
from bs4 import BeautifulSoup

# The idea of this code is compile all quotes from "Quotes to Scrape", their authors and their tags

url = 'https://quotes.toscrape.com/'

if __name__ == '__main__':
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    print(2)

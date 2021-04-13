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
    # To get all quotes, just check the "span" tag and class = "text"
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    # As there are more than 1 tag per quote, get the div tag
    tags = soup.find_all('div', class_='tags')

    # To remove the html properties from the quotes
    for i in range(0, len(quotes)):
        print(quotes[i].text)
        print(authors[i].text)
        quoteTags = tags[i].find_all('a', class_='tag')
        for quoteTag in quoteTags:
            print(quoteTag.text)

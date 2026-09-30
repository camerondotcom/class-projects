"""
Name: Cameron Chen
Course: CS242 | Fall 2026
Project: Web Scraper
Description:
    This script fetches a web page and prints the text of its headline
    tags (h1, h2, h3). It is a simple example of how to use the requests
    library to get a page and BeautifulSoup to pull data out of the HTML.
"""

import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    # Try to fetch the page
    try:
        response = requests.get(url)

        # Parse the HTML and find all headline tags
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(['h1', 'h2', 'h3'])

        # If there are no headlines, let the user know
        if not headlines:
            print("No headlines found on the page.")
            return

        # Print up to 10 headlines
        print("Headlines from", url, "\n")
        count = 1
        for headline in headlines:
            if count > 10:
                break
            text = headline.text.strip()
            if text:
                print(count, ". ", text, sep="")
            count = count + 1

    # Handle any errors that come up
    except Exception as e:
        print("An error occurred:", e)


# Only run the scraper if this file is executed directly
if __name__ == "__main__":
    url = "https://news.ycombinator.com"
    scrape_headlines(url)

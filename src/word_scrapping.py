import requests
from bs4 import BeautifulSoup

def scrap_5_letter_words(file_path):
    page = requests.get('https://www.thefreedictionary.com/5-letter-words.htm') # Getting page HTML through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    
    words = soup.select("article ul li a") # Selecting all of the word in the article

    with open(file_path, "w") as f:
        for word in words:
            f.write(f"{word.text}\n")
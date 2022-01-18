import requests
from bs4 import BeautifulSoup

def scrap_5_letter_words_bestwordlist(file_path):
    root = "https://www.bestwordlist.com/5letterwordspage"
    pages = [root + str(i) + '.htm' for i in range(2, 15)]
    pages.insert(0, "https://www.bestwordlist.com/5letterwordspage.htm")
    
    for page in pages:
        web_page = requests.get(page) # Getting page HTML through request
        soup = BeautifulSoup(web_page.content, 'html.parser') # Parsing content using beautifulsoup
        words = soup.select("span.mot") # Selecting all of the word in the article

        with open(file_path, "a") as f:
            for balise in words:
                for word in balise.text.strip().split(' '):
                    f.write(f"{word.lower()}\n")


if __name__ == "__main__":
    scrap_5_letter_words_bestwordlist("../dictionnaries/5_letters_words.txt")
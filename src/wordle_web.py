import configparser
import time
import re
from wordle_player import Player1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def type_word(word):
    Elem.send_keys(word)
    Elem.send_keys(Keys.ENTER)

def get_hints(guess, guess_number):
    # Query hints from the web
    web_hints = [
        browser.execute_script(f"return document.querySelector('game-app').shadowRoot.querySelector('game-row:nth-child({guess_number})').shadowRoot.querySelector('game-tile:nth-child({i+1})')._state") 
        for i in range(5)
    ]
    # When the same letter appear multiple time wordle can consider it as absent if it is present in another position we refined hints with this information
    refined_hints = []
    for i, hint in enumerate(web_hints):
        if hint == "absent" and guess.count(guess[i]) > 1: 
            refined_hints.append("")
        else:
            refined_hints.append(hint)
    return refined_hints

if __name__ == "__main__":

    #Read Config
    config = configparser.ConfigParser()
    config.read('../config.ini')

    # Launch a browser on the Wordle main page
    browser = webdriver.Chrome(config['CHROMEDRIVER']['ChromedriverPath'])
    page = browser.get('https://www.powerlanguage.co.uk/wordle/') # Getting page HTML through request

    # Skip informations pop-up
    time.sleep(1)
    Elem = browser.find_element(By.TAG_NAME, 'html')
    Elem.click()
    time.sleep(1)

    # Load game dictionnary
    with open("../dictionnaries/5_letters_words.txt", "r") as f:
        word_list = [x[:-1] for x in f.readlines()]

    # Instanciate a player
    player = Player1(word_list)

    # Guess a maximum number of 6 times
    for i in range(6):
        guess = player.guess() # Ask the player to guess
        type_word(guess) # Type the guess in the web interface
        time.sleep(3)
        hints = get_hints(guess, i+1) # Get hints from the web
        player.analyse_hints(guess, hints) # Send hints to the player
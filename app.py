from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

RANDOM_WORD_API_URL = "https://random-word-api.herokuapp.com/word?number={random}"
DUCKDUCKGO_HTML_URL = "https://html.duckduckgo.com/html/?q={query}"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Hardcode URLs in case other APIs fail
backup_list = ['https://huckleberrycare.com/',
    'https://asheron.fandom.com/wiki/Home',
    'https://knowyourmeme.com/',
    'https://interestingengineering.com/'
]

def get_random_search_query():
    try:
        word_number = random.randint(1, 5)
        response = requests.get(RANDOM_WORD_API_URL.format(random=word_number))
        if response.status_code == 200:
            random_words = response.json()
            random_query = '+'.join(random_words)
            return random_query
        else:
            return None
    except Exception as e:
        print("Error fetching random word:", e)
        return None

def extract_first_result_url(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    result_divs = soup.select('div.result, div.web-result')
    if result_divs:
        first_result = result_divs[0]
        first_link = first_result.find('a', class_='result__a')
        if first_link:
            return first_link['href']
    return None

@app.route('/')
def get_first_result_url():
    # Fetch random search query
    random_query = get_random_search_query()
    if random_query:
        # Fetch DuckDuckGo search results page
        search_url = DUCKDUCKGO_HTML_URL.format(query=random_query)
        # print(search_url)
        response = requests.get(search_url, headers=headers)
        # print(response)
        if response.status_code == 200:
            # Extract URL from HTML content
            url = extract_first_result_url(response.content)
            if url:
                return jsonify({'url': url})
    else:
        url = random.choice(backup_list)
        return jsonify({'url': url})

if __name__ == '__main__':
    app.run()
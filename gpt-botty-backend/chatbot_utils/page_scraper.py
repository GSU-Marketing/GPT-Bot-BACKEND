
import requests
from bs4 import BeautifulSoup

def crawl_and_update():
    for url in ["https://graduate.gsu.edu/", "https://online.gsu.edu/"]:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        with open(f"data/scraped_{url.split('//')[1].split('.')[0]}.txt", "w") as f:
            f.write(soup.get_text())

from bs4 import BeautifulSoup
import requests

def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except:
        return ""

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def update_pages(urls):
    return [extract_text_from_html(fetch_html(url)) for url in urls]

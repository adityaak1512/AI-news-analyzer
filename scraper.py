import requests
from bs4 import BeautifulSoup

def get_news_articles(company, num_articles=10):
    url = f"https://www.google.com/search?q={company}+news&hl=en&gl=US&lr=lang_en&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return [{"error": "Failed to fetch news"}]

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")[:num_articles]

    return [{"title": a.text} for a in articles]
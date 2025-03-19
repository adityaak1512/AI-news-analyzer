<<<<<<< HEAD
from fastapi import FastAPI
from scraper import get_news_articles
from sentiment import analyze_sentiment, compare_sentiments
from summarizer import summarize_text
from tts import generate_hindi_tts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "News Analyzer API is running!"}

@app.get("/news")
def fetch_news(company: str):
    news = get_news_articles(company)
    return {"news": news}

@app.get("/sentiment")
def fetch_sentiment(company: str):
    news = get_news_articles(company)
    for article in news:
        article["sentiment"] = analyze_sentiment(article["title"])
        article["confidence"] = article["sentiment"]["score"]
    return {"sentiment_analysis": compare_sentiments(news)}

@app.get("/summarize")
def fetch_summary(company: str):
    news = get_news_articles(company)
    for article in news:
        article["summary"] = summarize_text(article["title"])
    return {"summaries": news}

@app.get("/tts")
def generate_tts(company: str):
    news = get_news_articles(company)
    summary_text = ". ".join(summarize_text(a["title"]) for a in news)
    tts_file = generate_hindi_tts(summary_text)
=======
from fastapi import FastAPI
from scraper import get_news_articles
from sentiment import analyze_sentiment, compare_sentiments
from summarizer import summarize_text
from tts import generate_hindi_tts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "News Analyzer API is running!"}

@app.get("/news")
def fetch_news(company: str):
    news = get_news_articles(company)
    return {"news": news}

@app.get("/sentiment")
def fetch_sentiment(company: str):
    news = get_news_articles(company)
    for article in news:
        article["sentiment"] = analyze_sentiment(article["title"])
        article["confidence"] = article["sentiment"]["score"]
    return {"sentiment_analysis": compare_sentiments(news)}

@app.get("/summarize")
def fetch_summary(company: str):
    news = get_news_articles(company)
    for article in news:
        article["summary"] = summarize_text(article["title"])
    return {"summaries": news}

@app.get("/tts")
def generate_tts(company: str):
    news = get_news_articles(company)
    summary_text = ". ".join(summarize_text(a["title"]) for a in news)
    tts_file = generate_hindi_tts(summary_text)
>>>>>>> e1e754f (Initial commit)
    return {"tts_file": tts_file}
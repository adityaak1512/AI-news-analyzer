from transformers import pipeline
from collections import Counter

sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_model(text)[0]
    return {
        "label": "Positive" if result["label"] == "POSITIVE" else "Negative",
        "score": round(result["score"], 2)
    }

def compare_sentiments(news_articles):
    sentiment_counts = Counter(article["sentiment"] for article in news_articles)
    return dict(sentiment_counts)
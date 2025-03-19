<<<<<<< HEAD
from scraper import get_news_articles
from sentiment import analyze_sentiment, compare_sentiments
from summarizer import summarize_text
from tts import generate_hindi_tts

def main():
    company = input("Enter company name: ")
    news = get_news_articles(company)

    if "error" in news[0]:
        print(news[0]["error"])
    else:
        for article in news:
            article["summary"] = summarize_text(article["title"])
            article["sentiment"] = analyze_sentiment(article["title"])

        print("\nNews Summary & Sentiment Analysis:")
        for article in news:
            print(f"\nTitle: {article['title']}")
            print(f"Summary: {article['summary']}")
            print(f"Sentiment: {article['sentiment']}")

        print("\nOverall Sentiment:")
        print(compare_sentiments(news))

        summary_text = ". ".join(a["summary"] for a in news)
        generate_hindi_tts(summary_text)
        print("\nHindi Speech Generated: output.mp3")

if __name__ == "__main__":
=======
from scraper import get_news_articles
from sentiment import analyze_sentiment, compare_sentiments
from summarizer import summarize_text
from tts import generate_hindi_tts

def main():
    company = input("Enter company name: ")
    news = get_news_articles(company)

    if "error" in news[0]:
        print(news[0]["error"])
    else:
        for article in news:
            article["summary"] = summarize_text(article["title"])
            article["sentiment"] = analyze_sentiment(article["title"])

        print("\nNews Summary & Sentiment Analysis:")
        for article in news:
            print(f"\nTitle: {article['title']}")
            print(f"Summary: {article['summary']}")
            print(f"Sentiment: {article['sentiment']}")

        print("\nOverall Sentiment:")
        print(compare_sentiments(news))

        summary_text = ". ".join(a["summary"] for a in news)
        generate_hindi_tts(summary_text)
        print("\nHindi Speech Generated: output.mp3")

if __name__ == "__main__":
>>>>>>> e1e754f (Initial commit)
    main()
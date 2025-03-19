<<<<<<< HEAD
import streamlit as st
import matplotlib.pyplot as plt
from scraper import get_news_articles
from sentiment import analyze_sentiment, compare_sentiments
from summarizer import summarize_text
from tts import generate_hindi_tts

st.title("AI News Analyzer")

company = st.text_input("Enter a company name:", key="company_input")

if st.button("Analyze News"):
    if not company:
        st.warning("Please enter a company name.")
    else:
        news = get_news_articles(company)
        if not news or "error" in news[0]:
            st.error(news[0].get("error", "Failed to fetch news."))
        else:
            for article in news:
                article["summary"] = summarize_text(article["title"])
                sentiment_result = analyze_sentiment(article["title"])
                article["sentiment"] = sentiment_result["label"]
                article["confidence"] = sentiment_result["score"]

            st.subheader("Sentiment Summary")
            st.write(compare_sentiments(news))

            st.subheader("News Analysis")
            for article in news:
                st.write(f"**{article['title']}**")
                st.write(f"{article['summary']}")
                st.write(f"Sentiment: {article['sentiment']} (Confidence: {article['confidence']:.2f})")
                st.write("---")

            summary_text = ". ".join(a["summary"] for a in news)
            tts_file = generate_hindi_tts(summary_text)
            st.audio(tts_file, format="audio/mp3")
            st.success("Hindi Speech Generated!")

            st.subheader("Sentiment Analysis Trends")
            sentiments = [article["sentiment"] for article in news]
            sentiment_counts = {"Positive": sentiments.count("Positive"), "Negative": sentiments.count("Negative")}

            fig, ax = plt.subplots()
            ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=["green", "red"])
=======
import streamlit as st
import matplotlib.pyplot as plt
from scraper import get_news_articles
from sentiment import analyze_sentiment, compare_sentiments
from summarizer import summarize_text
from tts import generate_hindi_tts

st.title("AI News Analyzer")

company = st.text_input("Enter a company name:", key="company_input")

if st.button("Analyze News"):
    if not company:
        st.warning("Please enter a company name.")
    else:
        news = get_news_articles(company)
        if not news or "error" in news[0]:
            st.error(news[0].get("error", "Failed to fetch news."))
        else:
            for article in news:
                article["summary"] = summarize_text(article["title"])
                sentiment_result = analyze_sentiment(article["title"])
                article["sentiment"] = sentiment_result["label"]
                article["confidence"] = sentiment_result["score"]

            st.subheader("Sentiment Summary")
            st.write(compare_sentiments(news))

            st.subheader("News Analysis")
            for article in news:
                st.write(f"**{article['title']}**")
                st.write(f"{article['summary']}")
                st.write(f"Sentiment: {article['sentiment']} (Confidence: {article['confidence']:.2f})")
                st.write("---")

            summary_text = ". ".join(a["summary"] for a in news)
            tts_file = generate_hindi_tts(summary_text)
            st.audio(tts_file, format="audio/mp3")
            st.success("Hindi Speech Generated!")

            st.subheader("Sentiment Analysis Trends")
            sentiments = [article["sentiment"] for article in news]
            sentiment_counts = {"Positive": sentiments.count("Positive"), "Negative": sentiments.count("Negative")}

            fig, ax = plt.subplots()
            ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=["green", "red"])
>>>>>>> e1e754f (Initial commit)
            st.pyplot(fig)
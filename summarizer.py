<<<<<<< HEAD
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text):
=======
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text):
>>>>>>> e1e754f (Initial commit)
    return summarizer(text, max_length=50, min_length=20, do_sample=False)[0]["summary_text"]
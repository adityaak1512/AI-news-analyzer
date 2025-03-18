# 🚀 AI News Analyzer

## 📌 Overview
AI News Analyzer is a web application and API that:
- 📰 **Scrapes news articles** about a company
- 📊 **Analyzes their sentiment** (Positive/Negative)
- ✍️ **Summarizes headlines**
- 🔊 **Converts summaries into Hindi speech**
- ⚡ **Provides an API & Web App for easy interaction**

## 🌟 Features
✅ **Real-time News Scraping** 📰
✅ **Sentiment Analysis** 📊
✅ **Text Summarization** ✍️
✅ **Hindi Text-to-Speech (TTS)** 🔊
✅ **FastAPI-based REST API** ⚡
✅ **Streamlit-based Web App** 🎨

## ⚙️ Installation
### Prerequisites
🔹 Python 3.7+

### Setup
1️⃣ Clone the repository:
   ```sh
   git clone <repository-url>
   cd ai-news-analyzer
   ```
2️⃣ Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
### ▶️ Running the API
Start the FastAPI server:
```sh
uvicorn api:app --reload
```
🔗 Access API docs at: `http://127.0.0.1:8000/docs`

### 🖥️ Running the Web Application
```sh
streamlit run app.py
```

### 🖥️ Command-Line Usage
```sh
python main.py
```

## 🔗 API Endpoints
| 🛠️ Method | 🌍 Endpoint | 📖 Description |
|--------|---------------|-------------|
| GET    | `/`           | 🩺 Health check |
| GET    | `/news?company=<name>` | 📰 Fetch latest news |
| GET    | `/sentiment?company=<name>` | 📊 Sentiment analysis |
| GET    | `/summarize?company=<name>` | ✍️ Summarize news |
| GET    | `/tts?company=<name>` | 🔊 Generate Hindi speech |

## 🏗️ Technology Stack
- 🐍 **Python** (FastAPI, Streamlit, BeautifulSoup, Transformers, gTTS)
- 🤖 **Machine Learning** for NLP tasks
- 🐳 **Docker** for containerization

## 📜 License
This project is licensed under the terms of the [LICENSE](./LICENSE).

## 👥 Contributors
- **[Aditya Arun Kumar]** 👨‍💻 - Developer

## 🚀 Future Enhancements
- 📡 Improve news scraping for detailed articles
- 🌍 Expand language support for summaries & speech synthesis
- 🗄️ Implement a database for storing analyzed news

## 🙌 Acknowledgments
- ❤️ Uses `Hugging Face Transformers` for NLP
- 📰 Thanks to `Google News` for aggregation

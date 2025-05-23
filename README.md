# Chat Log Summarizer

## 📘 Overview

The **Chat Log Summarizer** is a Python-based tool that analyzes conversations between a user and an AI assistant. It extracts key metrics and generates concise summaries based on the dialogue.

Using **TF-IDF (Term Frequency-Inverse Document Frequency)**, it identifies the most relevant keywords in the chat, determines the main topics of discussion, and logs structured summaries.

---

## ✨ Features

- ✅ Parses structured chat logs (user and AI messages).
- 📊 Counts the number of exchanges (total, user, and AI).
- 🧠 Identifies top keywords using TF-IDF (including bigrams).
- 📝 Generates a human-readable summary of each conversation.
- 📂 Supports analyzing multiple chat log files in a single run.
- 🔍 Automatically detects and skips empty or invalid chat logs.
- ⚡ Efficient keyword extraction with customizable parameters (e.g., `top_n` keywords).
- 🛠 Provides fallback mechanisms for cases where no keywords are extracted.

---

## 🧱 Requirements

This project requires Python **3.7+** and the following libraries:

- `numpy==2.2.6`
- `scikit-learn==1.6.1`
- `scipy==1.15.3`
- `joblib==1.5.0`
- `threadpoolctl==3.6.0`

---

## ⚙️ Installation & Setup

1. **Clone the repository** (or download the source files):

```
   git clone https://github.com/Tanjib-Rafi/chat-log-summarizer.git
```
```
   cd chat-log-summarizer
```

2. **Create a virtual environment**:

```
   python3 -m venv venv
```

```
source venv/bin/activate
```

3. **Install dependencies**:
```
pip install -r requirements.txt
```

4. **Run the script**:

```
python3 main.py
```


## 📂 File Structure:

```
📦 chat-log-summarizer
├─ .gitignore
├─ README.md
├─ analyzer.py
├─ main.py
├─ parser.py
├─ requirements.txt
└─ sample_logs
   ├─ ecommerce.txt
   ├─ no_talk.txt
   ├─ no_user_no_ai.txt
   ├─ stock_price.txt
   └─ war.txt
```


## ⚙️ Customization:

You can adjust keyword extraction sensitivity by modifying parameters like:

`top_n (number of keywords)`

`modifying unigrams and bigrams`

`min_df and max_df in the TF-IDF vectorizer`

`token_pattern to control which tokens are allowed (e.g., skip short words)`

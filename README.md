# 🏦 FinBot: Smart Banking Q&A Chatbot

FinBot is an intelligent Question & Answer chatbot designed to simulate human-like interactions for answering banking-related queries. Inspired by EVA (Electronic Virtual Assistant), this chatbot uses advanced Natural Language Processing techniques and pre-trained transformer models to deliver highly accurate and conversational responses.

## 💡 Features

- 🤖 Answer questions about KYC, loans, account management, and more
- 📚 Uses a semantic search engine for accurate matching
- 🧠 Built using Transformer-based NLP models (`sentence-transformers`)
- 🖥️ Frontend using [Streamlit](https://streamlit.io) for smooth UI
- 📦 Easily extendable knowledge base

---

## 🧠 How It Works

1. Predefined banking FAQs and answers are embedded using `SentenceTransformer`.
2. A user’s query is converted into a vector and compared with stored FAQ vectors using cosine similarity.
3. The closest match is returned as the answer.
4. The embeddings are saved as a `pickle` file and reused via `app.py`.

---

## 📁 Project Structure
```bash
FinBot-Smart-Banking-Q-A-Chatbot/
├── app.py                    # Streamlit-based web interface
├── chatbot_model.pkl         # Precomputed sentence embeddings
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── notebook/
    └── FinBot_Model_Training.ipynb  # Training & embedding generation
```

## 🛠️ Getting Started

Follow these steps to set up and run **FinBot** locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aditya301cs/FinBot-Smart-Banking-Q-A-Chatbot.git
cd FinBot-Smart-Banking-Q-A-Chatbot
```


### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
streamlit run app.py
```

import streamlit as st
import pickle
from sentence_transformers import SentenceTransformer, util

# Load the FAQ data and sentence embeddings from pickle
with open('chatbot_model.pkl', 'rb') as f:
    faq_dict, questions, question_embeddings = pickle.load(f)

# Load the same model used in training
model = SentenceTransformer('all-MiniLM-L6-v2')

# Chatbot logic: Semantic similarity + keyword fallback
def get_semantic_answer(user_query, threshold=0.6):
    user_embedding = model.encode(user_query, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(user_embedding, question_embeddings)
    top_score, top_idx = similarity_scores[0].max(0)

    if top_score.item() > threshold:
        matched_question = questions[top_idx]
        return faq_dict[matched_question]
    else:
        return None

def keyword_fallback(query):
    for question, answer in faq_dict.items():
        if any(word in question.lower() for word in query.lower().split()):
            return answer
    return "❌ Sorry, I couldn't understand your query. Please contact customer care."

def chatbot_response(query):
    answer = get_semantic_answer(query)
    if answer:
        return answer
    else:
        return keyword_fallback(query)

# Streamlit UI
st.set_page_config(page_title="FinBot: Smart Banking Q&A Chatbot", page_icon="🤖", layout="centered")

st.title("FinBot: Smart Banking Q&A Chatbot")
st.write("Ask any banking-related question below:")

user_input = st.text_input("🔎 Your Question:")

if user_input:
    reply = chatbot_response(user_input)
    st.success(reply)

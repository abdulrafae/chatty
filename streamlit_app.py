# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st
import requests

tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

with st.sidebar:
     "[View the source code](https://github.com/abdulrafae/chatty/blob/main/streamlit_app.py)"

st.title("💬 Chatty")
st.caption("🚀 A custom chatbot powered by BlenderBot LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
    
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = query({"inputs":prompt})
    msg = response #response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

import streamlit as st

st.set_page_config(page_title="Medical Chatbot", layout="centered")

st.title("Multimodal Medical Chatbot (Zeroth Review Prototype)")
st.write("Initial prototype for a RAG-based healthcare chatbot.")

user_input = st.text_input("Enter your symptoms:")

if user_input:
    st.write("Response generation will be implemented in future reviews.")

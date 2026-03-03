import streamlit as st
import pickle

st.title("📧 Spam Email Detector")

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

msg = st.text_area("Enter your message")

if st.button("Predict"):
    vec = vectorizer.transform([msg])
    pred = model.predict(vec)[0]

    if pred == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")
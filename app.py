import streamlit as st
import pickle
st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4CAF50;
}
.sub-text {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📧 Spam Email Detector</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">AI-powered SMS & Email Classifier</p>', unsafe_allow_html=True)

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

msg = st.text_area(
    "✉️ Enter your message",
    height=150,
    placeholder="Type your message here..."
)
predict_btn = st.button("🔍 Analyze Message", use_container_width=True)
if predict_btn and msg.strip() != "":

    clean_msg = clean_text(msg)
    vec = vectorizer.transform([clean_msg])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]
    confidence = max(prob) * 100

    st.markdown("---")

    if pred == 1:
        st.error(f"🚨 **Spam Message** ({confidence:.2f}% confidence)")
    else:
        st.success(f"✅ **Not Spam** ({confidence:.2f}% confidence)")

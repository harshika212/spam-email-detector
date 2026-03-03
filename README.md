# 📧 Spam Email Detector

An AI-powered web application that classifies SMS/Email messages as **Spam** or **Not Spam** using Natural Language Processing and Machine Learning.

🔗 **Live App:** https://spam-email-detector-mnqmnz3s2gq2kd7cr7cgnc.streamlit.app/

---

## 🚀 Features

- 🔍 Real-time spam detection  
- 🧠 TF-IDF based text vectorization  
- 🤖 Machine Learning classification  
- 🎨 Interactive Streamlit web interface  
- 📊 Confidence score display  
- 🌐 Deployed on Streamlit Cloud  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- NLP (TF-IDF, NLTK)  
- Streamlit  
- NumPy & Pandas  

---

## 📂 Project Structure

```
spam-email-detector/
│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User enters a message  
2. Text is cleaned and preprocessed  
3. TF-IDF converts text to numerical features  
4. Trained ML model predicts spam/ham  
5. Result shown with confidence score  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 📊 Model Performance

- Algorithm: Logistic Regression / Naive Bayes  
- Feature Engineering: TF-IDF (unigrams + bigrams)  
- Accuracy: ~97–99% on test data  

---

## 🌟 Future Improvements

- Deep learning model (LSTM/BERT)  
- Email subject + body support  
- Multilingual spam detection  
- Improved UI themes  

---

## 👩‍💻 Author

**Harshika**  
GitHub: https://github.com/harshika212

---

⭐ If you found this project useful, consider starring the repo!

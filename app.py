import streamlit as st
from model import predict_sentiment
from utils import detect_issue
import matplotlib.pyplot as plt

st.title("Customer Experience Analytics Platform")

user_input = st.text_area("Enter customer review:")

if st.button("Analyze"):

    # Sentiment
    sentiment = predict_sentiment(user_input)
    st.subheader("Sentiment")
    st.write(sentiment)

    # Issue detection
    issue = detect_issue(user_input)
    st.subheader("Issue Detected")
    st.write(issue)

    # Chart
    labels = ["Positive", "Negative", "Neutral"]
    values = [10, 10, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')

    st.subheader("Sentiment Distribution")
    st.pyplot(fig)
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#Load dataset
data = pd.read_csv("reviews_dataset.csv")

#Clean column names
data.columns = data.columns.str.strip().str.lower()

X = data["review"]
y = data["sentiment"]

# Cnvert tect to numbers
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

#Train model
model = LogisticRegression()
model.fit(X_vec, y)

#Prediction function
def predict_sentiment(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]

print(data.columns.tolist())

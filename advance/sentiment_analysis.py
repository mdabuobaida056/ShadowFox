import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download stopwords (only first time)
nltk.download("stopwords")

# Sample dataset
data = {
    "text": [
        "I love this internship",
        "This project is amazing",
        "I feel very happy",
        "This is terrible",
        "I hate this task",
        "Very disappointing experience"
    ],
    "label": [1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

# Clean text function
def clean_text(text):
    text = text.lower()
    text = "".join(char for char in text if char not in string.punctuation)
    return text

df["clean_text"] = df["text"].apply(clean_text)

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words=stopwords.words("english"))
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

print("Model trained successfully!")

# User input loop
while True:
    user_input = input("\nEnter sentence (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting program.")
        break

    if user_input.strip() == "":
        print("Please enter valid text.")
        continue

    user_clean = clean_text(user_input)
    user_vector = vectorizer.transform([user_clean])

    prediction = model.predict(user_vector)

    if len(prediction) > 0:
        if prediction[0] == 1:
            print("Sentiment: Positive 😊")
        else:
            print("Sentiment: Negative 😞")
    else:
        print("Prediction failed.")

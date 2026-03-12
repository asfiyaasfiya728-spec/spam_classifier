import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only needed columns
data = data[['v1','v2']]
data.columns = ['label','message']

# Convert labels
data['label'] = data['label'].map({'ham':0,'spam':1})

# Split data
X = data['message']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Convert text to numbers
vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Test your own message
msg = ["Congratulations! You won a free prize"]

msg_vector = vectorizer.transform(msg)

result = model.predict(msg_vector)

if result[0] == 1:
    print("Spam Message")
else:
    print("Not Spam")

# Save model and vectorizer
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully!")
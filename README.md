# 📧 Spam Classifier Web App

## 📌 Project Overview
Spam messages create productivity and security issues.  
This project is a **Machine Learning-based Spam Detection Web Application** built using Flask that classifies emails as **Spam** or **Not Spam**.

The application allows users to input email subject and message content, predicts the result instantly, and stores the classification history.

---

## 🎯 Problem Statement
Unwanted spam emails can waste time and pose security risks.  
This system helps automatically detect spam emails using a trained machine learning model.

---

## 🛠️ Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- HTML
- Bootstrap
- Matplotlib

---

## 🧠 Machine Learning Model
- Logistic Regression
- Text Vectorization using CountVectorizer / TfidfVectorizer

---

## 🚀 Features
- Classify emails instantly
- View classification history
- Download history as CSV
- Visualize Spam vs Not Spam with charts
- Simple and clean web interface

---

## 📂 Project Structure
```
spam_classifier/
│
├── data/
│   └── spam.csv
│
├── models/
│   └── spam_model.pkl
│
├── templates/
│   ├── index.html
│   ├── history.html
│
├── static/
│   └── styles.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🖥️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/asfiyaasfiya728-spec/spam_classifier.git
```

### 2️⃣ Navigate into the project folder
```bash
cd spam_classifier
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application
```bash
python app.py
```

### 5️⃣ Open in browser
```
http://127.0.0.1:5000/
```

---

## 📊 Sample Output

```
![App Screenshot](screenshot.png)
```

---

## 🔮 Future Improvements
- Deploy to cloud (Render / Railway)
- Add user authentication
- Improve UI design
- Use advanced NLP techniques

---

## 👩‍💻 Author
**Asfiya A**  
Aspiring Python & Machine Learning Developer  

from flask import Flask, render_template, request, Response, redirect, url_for, session
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "yoursecretkey123"   # change this to any random string
spam_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        subject = request.form["subject"]
        message = request.form["message"]

        # Run spam detection
        prediction, confidence = run_spam_model(subject, message)

        # Save to history with timestamp
        spam_history.append({
            "subject": subject,
            "message": message,
            "prediction": prediction,
            "confidence": confidence,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return render_template("index.html",
                           prediction=prediction,
                           confidence=confidence)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ✅ Update these to your own credentials
        if username == "asfiya@gmail.com" and password == "mysecurepass":
            session["logged_in"] = True
            return redirect(url_for("history"))
        else:
            return "Invalid credentials. Try again."
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

@app.route("/history")
def history():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    spam_count = sum(1 for item in spam_history if item["prediction"] == "Spam")
    not_spam_count = sum(1 for item in spam_history if item["prediction"] == "Not Spam")
    return render_template("history.html", history=spam_history,
                           spam_count=spam_count, not_spam_count=not_spam_count)

@app.route("/download")
def download():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    def generate():
        data = [["Subject", "Message", "Prediction", "Confidence", "Time"]]
        for item in spam_history:
            data.append([item["subject"], item["message"], item["prediction"], item["confidence"], item["time"]])
        output = ""
        for row in data:
            output += ",".join(map(str, row)) + "\n"
        return output

    return Response(generate(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=spam_report.csv"})

def run_spam_model(subject, message):
    spam_keywords = ["free", "win", "prize", "money", "urgent", "click"]
    text = (subject + " " + message).lower()
    if any(word in text for word in spam_keywords):
        return "Spam", 95
    else:
        return "Not Spam", 90

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

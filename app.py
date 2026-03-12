from flask import Flask, render_template, request, Response
import csv
import os

app = Flask(__name__)
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

        # Save to history
        spam_history.append({
            "subject": subject,
            "message": message,
            "prediction": prediction,
            "confidence": confidence
        })

    return render_template("index.html",
                           prediction=prediction,
                           confidence=confidence)

@app.route("/history")
def history():
    spam_count = sum(1 for item in spam_history if item["prediction"] == "Spam")
    not_spam_count = sum(1 for item in spam_history if item["prediction"] == "Not Spam")
    return render_template("history.html", history=spam_history,
                           spam_count=spam_count, not_spam_count=not_spam_count)

@app.route("/download")
def download():
    def generate():
        data = [["Subject", "Message", "Prediction", "Confidence"]]
        for item in spam_history:
            data.append([item["subject"], item["message"], item["prediction"], item["confidence"]])
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
    port = int(os.environ.get("PORT", 5000))  # important for deployment
    app.run(host="0.0.0.0", port=port)

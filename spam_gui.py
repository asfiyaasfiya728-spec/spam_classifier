import tkinter as tk
import pickle

# Load saved model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Function to check spam
def check_spam():
    message = entry.get()

    message_vector = vectorizer.transform([message])

    result = model.predict(message_vector)

    if result[0] == 1:
        output_label.config(text="Spam Message", fg="red")
    else:
        output_label.config(text="Not Spam", fg="green")

# Create window
window = tk.Tk()
window.title("Spam Detection App")
window.geometry("400x200")

# Input field
entry = tk.Entry(window, width=50)
entry.pack(pady=20)

# Button
check_button = tk.Button(window, text="Check Message", command=check_spam)
check_button.pack()

# Output label
output_label = tk.Label(window, text="")
output_label.pack(pady=20)

# Run application
window.mainloop()
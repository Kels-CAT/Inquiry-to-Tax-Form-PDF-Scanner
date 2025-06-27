from flask import Flask, render_template, request
from nlp.analyzer import extract_keywords

app = Flask(__name__)  # ← must be defined BEFORE using @app.route

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        inquiry = request.form["inquiry"]
        print("Inquiry received from form:", inquiry)
        results = extract_keywords(inquiry)
        print("Results returned by extract_keywords():", results)

    return render_template("index.html", results=results)





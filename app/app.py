from flask import Flask, render_template, request
from app.nlp.analyzer import extract_keywords

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        inquiry = request.form["inquiry"]
        results = extract_keywords(inquiry)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

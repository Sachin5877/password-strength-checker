from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def strength_score(p):
    score = 0
    score += len(p) >= 10
    score += bool(re.search(r"[A-Z]", p))
    score += bool(re.search(r"[a-z]", p))
    score += bool(re.search(r"\d", p))
    score += bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", p))
    return score

def strength_label(score):
    return {
        0: ("Very Weak", "red"),
        1: ("Weak", "red"),
        2: ("Fair", "orange"),
        3: ("Good", "gold"),
        4: ("Strong", "lightgreen"),
        5: ("Excellent", "green")
    }.get(score, ("Unknown", "grey"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    pw = request.json.get("password", "")
    score = strength_score(pw)
    label, color = strength_label(score)
    return jsonify({"label": label, "color": color, "score": score})

if __name__ == "__main__":
    app.run(debug=True)

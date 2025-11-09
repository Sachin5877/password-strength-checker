from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"[@$!%*?&#]", pw):
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score == 3 or score == 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    pw = data.get('password', '')
    result = check_strength(pw)
    return jsonify({'strength': result})

if __name__ == '__main__':
    app.run(debug=True)

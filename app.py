from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = "Weak"
    if len(password) >= 8:
        strength = "Medium"
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        strength = "Strong"
    return strength

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
        return render_template("result.html", strength=strength)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
    

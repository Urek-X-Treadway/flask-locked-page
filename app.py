from flask import Flask, render_template, request, redirect

app = Flask(__name__)
CORRECT_PASSWORD = "1234"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == CORRECT_PASSWORD:
            return redirect("/secret")
        else:
            return redirect("/denied")
    return render_template("login.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")

if __name__ == "__main__":
    app.run()


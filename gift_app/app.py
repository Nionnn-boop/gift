from flask import Flask, render_template, request

app = Flask(__name__)

PASSWORD = "manel123"

@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        entered = request.form.get("password")

        if entered == PASSWORD:
            return render_template("index.html")
        else:
            error = "Wrong password. Try again 💜"

    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
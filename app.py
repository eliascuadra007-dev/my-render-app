from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "World")
    return render_template("home.html", name=name)

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/square/<int:n>")
def square(n):
    return {
        "number": n,
        "square": n * n
    }

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home page – shows dynamic message
@app.route("/")
def home():
    name = request.args.get("name", "World")
    return render_template_string("""
        <h1>Hello, {{ name }}!</h1>
        <p>This is a free dynamic site running on Render.</p>
        <p>Try adding <code>?name=Elias</code> to the URL.</p>
    """, name=name)


# Another dynamic route
@app.route("/square/<int:n>")
def square(n):
    return {
        "number": n,
        "square": n * n
    }


if __name__ == "__main__":
    app.run(debug=True)

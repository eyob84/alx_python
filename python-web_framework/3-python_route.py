from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
@app.route('/c', strict_slashes=False)
def display_c_text(text=""):
    text = text.replace('_', ' ') if text else "is cool"
    return f"C {text}"

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def display_python_text(text=""):
    text = text.replace('_', ' ') if text else "is cool"
    return f"Python {text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


__doc__ = """
this is documentation for my module
"""
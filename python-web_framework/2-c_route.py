from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    text = text.replace('_', ' ')  # Replace underscore with space
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


__doc__ = """
this is documentation for my module
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Simple flask web application
    """
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

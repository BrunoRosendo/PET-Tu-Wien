from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    print(f"Received a request: {request}")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)

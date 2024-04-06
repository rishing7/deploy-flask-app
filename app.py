from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/todo")
def todo():
    return jsonify({"name": "rishi", "age": 26})


@app.route("/todo_post", methods=["POST"])
def todo_post():
    return jsonify({"name": "rishi", "age": 26})


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    msg = "user 1: "
    msg += ", user2: "
    return msg + "Hello, World!"


if __name__ == "__main__":
    app.run()

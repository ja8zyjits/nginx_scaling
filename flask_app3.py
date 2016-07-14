from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world server 3" 


if __name__ == "__main__":
    app.run(port=8002)

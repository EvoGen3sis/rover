from flask import Flask
from motor import Motor

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/motor", methods = ["POST"])




app.route("/feed", )


if __name__ == "__main__":
    app.run(debug = True)

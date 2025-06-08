from flask import Flask
from flask_cors import CORS
from motor import Motor

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/motor/<directions>", methods = ["POST"])




app.route("/feed", )


if __name__ == "__main__":
    app.run(debug = True)

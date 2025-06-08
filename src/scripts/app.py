from flask import Flask, request, jsonify, send_from_directory, render_template
from motor import forwards, left, right, backwards, halt
from flask_cors import CORS
import os

app = Flask(__name__, 
    static_folder="static",
    template_folder="templates")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/motor/<directions>", methods = ["POST"])
def __init__(self):
    pass



#app.route("/feed", )
@app.route("/scripts/<path:filename>")
def serve_script(filename):
    return send_from_directory("scripts", filename)

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

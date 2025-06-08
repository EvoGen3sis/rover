from flask import Flask, request, jsonify, send_from_directory, render_template
from demo import forwards, left, right, backwards, halt
#from motor import forwards, left, right, backwards, halt
from flask_cors import CORS
import os

app = Flask(__name__, 
    static_folder="static",
    template_folder="templates")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

direction_handlers = {"forwards": forwards(), 
    "left": left(), 
    "right": right(), 
    "backwards": backwards(), 
    "halt": halt()
}

@app.route("/motor", methods=["POST"])
def motor_control():
    data = request.get_json()
    direction = data.get("direction")

    handler = direction_handlers.get(direction)

    if handler:
        handler()
        return jsonify({"status": "OK", "direction": direction})
    else:
        return jsonify({"error": "Invalid direction"}), 400


#app.route("/feed", )

@app.route("/scripts/<path:filename>")
def serve_script(filename):
    return send_from_directory("scripts", filename)

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

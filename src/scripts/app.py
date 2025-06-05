from flask import Flask
#from motor import 

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/motor")
def __init__(self):
    self.directions = ["forwards", "left", "right", "backwards", "halt"]

def motor(self):
    pass


if __name__ == "__main__":
    app.run(debug = True)

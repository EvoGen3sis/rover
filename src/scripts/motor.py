from flask import Flask, render_template_string, request, Response
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview
import cv2
import io
import time

# === GPIO Setup ===
LEFT_MOTOR_FORWARD = 17
LEFT_MOTOR_BACKWARD = 18
RIGHT_MOTOR_FORWARD = 22
RIGHT_MOTOR_BACKWARD = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [LEFT_MOTOR_FORWARD, LEFT_MOTOR_BACKWARD, RIGHT_MOTOR_FORWARD, RIGHT_MOTOR_BACKWARD]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# === Camera Setup ===
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
picam2.start()

# === Flask Setup ===
app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Robot Control with Video</title>
    <style>
        body { text-align: center; font-family: sans-serif; }
        button {
            width: 100px; height: 60px;
            font-size: 16px; margin: 10px;
        }
        img {
            width: 640px;
            height: 480px;
            border: 2px solid #555;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Robot Control with Video</h1>
    <img src="{{ url_for('video_feed') }}" alt="Video Stream">
    <form action="/" method="post">
        <div>
            <button name="action" value="forward">Forward</button>
        </div>
        <div>
            <button name="action" value="left">Left</button>
            <button name="action" value="stop">Stop</button>
            <button name="action" value="right">Right</button>
        </div>
        <div>
            <button name="action" value="backward">Backward</button>
        </div>
    </form>
</body>
</html>
"""

# === Motor Control Functions ===
def stop():
    for pin in MOTOR_PINS:
        GPIO.output(pin, GPIO.LOW)

def move_forward():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.LOW)

def move_backward():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.HIGH)

def turn_left():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.LOW)

def turn_right():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.HIGH)

# === Flask Routes ===
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "forward":
            move_forward()
        elif action == "backward":
            move_backward()
        elif action == "left":
            turn_left()
        elif action == "right":
            turn_right()
        elif action == "stop":
            stop()
    return render_template_string(HTML_TEMPLATE)

def gen_frames():
    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

# === Run Server ===
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=False)
    finally:
        stop()
        GPIO.cleanup()
        picam2.stop()

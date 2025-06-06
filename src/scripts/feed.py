import socket

class Feed:
    
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
    picam2.start()

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

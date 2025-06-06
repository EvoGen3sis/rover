try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    raise ImportError("RPi.GPIO not found. Make sure you are running this on a Raspberry Pi.")

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.lmf = 17
        self.lmb = 18
        self.rmf = 22
        self.rmb = 23
        self.pins = [self.lmf, self.lmb, self.rmf, self.rmb]

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            
    def forwards(self):
        GPIO.output(self.lmf, GPIO.HIGH)
        GPIO.output(self.lmb, GPIO.LOW)
        GPIO.output(self.rmf, GPIO.HIGH)
        GPIO.output(self.rmb, GPIO.LOW)

    def left(self):
        GPIO.output(self.lmf, GPIO.LOW)
        GPIO.output(self.lmb, GPIO.HIGH)
        GPIO.output(self.rmf, GPIO.HIGH)
        GPIO.output(self.rmb, GPIO.LOW)

    def right(self):
        GPIO.output(self.lmf, GPIO.HIGH)
        GPIO.output(self.lmb, GPIO.LOW)
        GPIO.output(self.rmf, GPIO.LOW)
        GPIO.output(self.rmb, GPIO.HIGH)

    def backwards(self):
        GPIO.output(self.lmf, GPIO.LOW)
        GPIO.output(self.lmb, GPIO.HIGH)
        GPIO.output(self.rmf, GPIO.LOW)
        GPIO.output(self.rmb, GPIO.HIGH)

    def halt(self):
        for i in self.pins:
            GPIO.output(i, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

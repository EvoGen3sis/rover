try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    pass

class Motor:
    def __init__(self):
        self.lmf = 17
        self.lmb = 18
        self.rmf = 22
        self.rmb = 23
        self.pins = [self.lmf, self.lmb, self.rmf, self.rmb]
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
            
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

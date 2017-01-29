import time
import atexit
import RPi.GPIO as GPIO
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor_input_pin = 21
sensor_output_pin = 20

# Setup the sensor pins
#GPIO.setup(sensor_input_pin, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor_input_pin, GPIO.IN)
GPIO.setup(sensor_output_pin, GPIO.OUT)
GPIO.output(sensor_output_pin, 1);

# create a motor hat object
mh = Adafruit_MotorHAT(addr=0x60)

# auto-disable motors on shutdown
def stopAll():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    GPIO.output(sensor_output_pin, 0);

atexit.register(stopAll)

# Get the motor to spin
myMotor = mh.getMotor(1)

# Sleep half a second before we start anything
time.sleep(0.5)

# Start the motor
myMotor.setSpeed(150)
myMotor.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
# myMotor.run(Adafruit_MotorHAT.RELEASE);

while True:
  button_state = GPIO.input(sensor_input_pin)
  if button_state == GPIO.HIGH:
    print ("HIGH")
    myMotor.setSpeed(0);
  else:
    print ("LOW")
    myMotor.setSpeed(150);
  time.sleep(0.5)

import RPi.GPIO as GPIO
import httplib, time

TIMEOUT = 5.0 #seconds
API_HOST = "hackerspace.idi.ntnu.no"
API_ENDPOINT = "/api/door"
GPIO_PIN = 7

class Door:
  # Initialize state to 1 (door closed)
  state = 1

  def check():
    # Read state from GPIO.
    gpio = GPIO.input(GPIO_PIN)

    if self.state != gpio:
      # State has changed, create connection to API.
      conn = httplib.HTTPConnection(API_HOST)

      if gpio == 1:
        conn.request('PUT', API_ENDPOINT)
        print "Door closed"
      else:
        conn.request('POST', API_ENDPOINT)
        print "Door open"
    self.state = gpio

if __name__ == '__main__':
  # Initialize the GPIO.
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

  # Class representing a door, and its state.
  door = Door()

  # Add interrupt handler for the GPIO.
  GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=lambda x: d.check(), bouncetime=300)

  # Run forever.
  while True:
    pass

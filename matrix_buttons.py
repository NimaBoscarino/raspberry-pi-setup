from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
from signal import pause
import requests
from gpiozero import Button

phone = []

def callNumber():
  global phone
  url = 'https://morse-signal.herokuapp.com/callNumber/' + ''.join(phone)
  print(url)
  response = requests.get('https://morse-signal.herokuapp.com/callNumber/' + ''.join(phone))
  message = response.text
  print(message)
  phone = []

GPIO.setwarnings(False) 

# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

ROW_PINS = [0,5,6,13] # BCM numbering
COL_PINS = [19,26,20,21] # BCM numbering


factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def processKey(key):
  print(key)
  if (key == 'A'):
    callNumber()
  else:
    phone.append(key)
    print(phone)

keypad.registerKeyPressHandler(processKey)

print('Press some keys, then press A to call!')

pause()

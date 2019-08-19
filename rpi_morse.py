import RPi.GPIO as GPIO
import time
import json

class Config:
  def __init__(self, json):
    self.unit = json['unit']
    self.buzzer_pin = json['buzzer_pin']
    self.led_pin = json['led_pin']
    self.morse_code_map_file_path = json['morse_code_map_file_path']

def load_config():
  with open("./config.json") as file:
    return Config(json.load(file))

def load_morse_map(file_path):
  with open(file_path) as file:
    return json.load(file)

def initialize_pi_board():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  GPIO.setup(led_pin, GPIO.OUT)
  GPIO.setup(buzzer_pin, GPIO.OUT)

def cleanup():
  buzzer_pwm.stop()
  GPIO.cleanup()

def turn_off_light():
  print('beep off')
  GPIO.output(led_pin, GPIO.LOW)
  buzzer_pwm.ChangeDutyCycle(0)

def turn_on_light():
  print('beep on')
  GPIO.output(led_pin, GPIO.HIGH)
  buzzer_pwm.ChangeDutyCycle(1)

def run_letter(letter):
  code_str = morse_map.get(letter, "..--..")
  print(letter + " : " + code_str)
  for index, part in enumerate(code_str):
    turn_on_light()
    run_length = dot_length if (part == ".") else dash_length
    beep_type = 'dot' if (part == ".") else 'dah'
    print('sleep for ' + beep_type + ' length: ' + str(run_length))
    time.sleep(run_length)
    turn_off_light()
    if index != len(code_str) - 1:
      print('sleep for part space length: ' + str(part_space_length))
      time.sleep(part_space_length)


def run_message(message):
  words = message.split()
  for word_index, word in enumerate(words):
    print(word)
    for letter_index, letter in enumerate(word):
      run_letter(letter.lower())
      if letter_index != len(word) - 1:
        print('sleep for letter space length: ' + str(letter_space_length))
        time.sleep(letter_space_length)
    if word_index != len(words) - 1:
      print('sleep for word space length: ' + str(word_space_length))
      time.sleep(word_space_length)

config = load_config()
morse_map = load_morse_map(config.morse_code_map_file_path)

# define units and lengths of morse code
unit = config.unit
dot_length = 1.0 * unit
dash_length = 3.0 * unit
part_space_length = 1.0 * unit
letter_space_length = 3.0 * unit
word_space_length = 7.0 * unit

# define board constants
led_pin = config.led_pin
buzzer_pin = config.buzzer_pin

initialize_pi_board()
buzzer_pwm = GPIO.PWM(buzzer_pin, 523)
buzzer_pwm.start(0)



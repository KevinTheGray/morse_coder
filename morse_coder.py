# import RPi.GPIO as GPIO
import time
import sys
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
buzzer_pwm = None

def validate_arguments():
	if len(sys.argv) < 2:
		print("Usage: morse_lights.py <message>")
		exit(-1)

def initialize_pi_board():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setup(buzzer_pin, GPIO.OUT)

def turn_off_light():
	GPIO.output(led_pin, GPIO.LOW)
	buzzer_pwm.ChangeDutyCycle(0)

def turn_on_light():
	GPIO.output(led_pin, GPIO.HIGH)
	buzzer_pwm.ChangeDutyCycle(1)

def start_countdown(message):
	print("Signaling \"" + message + "\" in 2...")
	time.sleep(1.0)
	print("1...")
	time.sleep(1.0)
	print("NOW!")

def run_letter(letter):
	code_str = morse_map.get(letter, "..--..")
	print(letter + " : " + code_str)
	for index, part in enumerate(code_str):
		turn_on_light()
		run_length = dot_length if (part == ".") else dash_length
		time.sleep(run_length)
		turn_off_light()
		if index != len(code_str) - 1:
			time.sleep(part_space_length)


def run_message(message):
	words = message.split()
	for word in words:
		print(word)
		for letter in word:
			run_letter(letter.lower())
			turn_off_light()
			time.sleep(letter_space_length)
		turn_off_light()
		time.sleep(word_space_length)

def cleanup():
	buzzer_pwm.stop()
	GPIO.cleanup()

# main
validate_arguments()
initialize_pi_board()
buzzer_pwm = GPIO.PWM(buzzer_pin, 523)
buzzer_pwm.start(0)
message = str(sys.argv[1])
morse_map = load_morse_map()
start_countdown(message)
run_message(message)
cleanup()

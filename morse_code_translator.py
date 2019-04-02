import RPi.GPIO as GPIO
import time
import sys
import json

# define units and lengths of morse code
unit = 0.05
dot_length = 1.0 * unit
dash_length = 3.0 * unit
part_space_length = 1.0 * unit
letter_space_length = 3.0 * unit
word_space_length = 7.0 * unit

#define the global morse map
morse_map = {}

# define board constants
led_pin = 16
buzzer_pin = 12
buzzer_pwm = None

def validate_arguments():
	if len(sys.argv) < 2:
		print("Usage: morse_lights.py <message>")
		exit(-1)

def load_morse_map():
	with open("./morse_code_defs/international_morse_code.json") as file:
		return json.load(file)

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

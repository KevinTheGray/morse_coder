import rpi_morse as rpi_morse
import sys

def validate_arguments():
  if len(sys.argv) < 2:
    print("Usage: morse_lights.py <message>")
    exit(-1)

validate_arguments()
message = str(sys.argv[1])
rpi_morse.run_message(message)
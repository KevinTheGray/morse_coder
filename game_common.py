import rpi_morse as rpi_morse
import sys
import random
import time

def getYesOrNoAnswer(prompt): 
  answer = raw_input(prompt)
  return False if answer.lower() == 'n' else True

def playRound(message, answer_prompt):
  print('=========================================');
  print('Get ready!');
  time.sleep(0.30)
  print('3...');
  time.sleep(0.30)
  print('2...');
  time.sleep(0.30)
  print('1...');
  time.sleep(0.30)
  rpi_morse.run_message(message)
  userInput = raw_input(answer_prompt)
  if (len(userInput) == 0):
    return playRound(message, answer_prompt)
  correct = userInput.lower() == message
  if (correct):
    print('Correct! It was ' + message + '!')
  else:
    print('Incorrect! It was ' + message + '!')
  print('=========================================');
  return correct
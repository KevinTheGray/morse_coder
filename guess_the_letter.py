import rpi_morse as rpi_morse
import sys
import random
import time

lettersList = rpi_morse.morse_map.keys()
lettersList.remove('?')

def getYesOrNoAnswer(prompt): 
  answer = raw_input(prompt)
  return False if answer.lower() == 'n' else True

def playRound():
  print('=========================================');
  print('Get ready!');
  time.sleep(0.40)
  print('3...');
  time.sleep(0.40)
  print('2...');
  time.sleep(0.40)
  print('1...');
  time.sleep(0.40)
  randomLetter = random.choice(lettersList)
  rpi_morse.run_message(randomLetter)
  userInput = raw_input('What letter was that? ')
  correct = userInput.lower() == randomLetter
  if (correct):
    print('Correct! It was ' + randomLetter + '!')
  else:
    print('Incorrect! It was ' + randomLetter + '!')
  print('=========================================');
  return correct

playing = getYesOrNoAnswer("Ready? (y/n) ")
totalPlayed = 0
numCorrect = 0

while(playing):
  totalPlayed += 1
  numCorrect += 1 if playRound() else 0
  playing = getYesOrNoAnswer('Play another round? (y/n) ')
print('You got ' + str(numCorrect) + ' correct out of ' + str(totalPlayed) + '.') 
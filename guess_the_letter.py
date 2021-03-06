import rpi_morse as rpi_morse
import game_common as game_common
import sys
import random
import time

lettersList = rpi_morse.morse_map.keys()
lettersList.remove('?')

def getRandomLetter():
  return random.choice(lettersList)

playing = game_common.getYesOrNoAnswer("Ready? (y/n) ")
totalPlayed = 0
numCorrect = 0

while(playing):
  totalPlayed += 1
  numCorrect += 1 if game_common.playRound(getRandomLetter(), 'What letter was that? ') else 0
  playing = game_common.getYesOrNoAnswer('Play another round? (y/n) ')
print('You got ' + str(numCorrect) + ' correct out of ' + str(totalPlayed) + '.') 
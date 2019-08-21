import rpi_morse as rpi_morse
import game_common as game_common
import sys
import random
import time

lines = [line.rstrip('\n') for line in open('words.txt')]

def getRandomWord():
  return random.choice(lines)

playing = game_common.getYesOrNoAnswer("Ready? (y/n) ")
totalPlayed = 0
numCorrect = 0

while(playing):
  totalPlayed += 1
  numCorrect += 1 if game_common.playRound(getRandomWord(), 'What word was that? ') else 0
  playing = game_common.getYesOrNoAnswer('Play another round? (y/n) ')
print('You got ' + str(numCorrect) + ' correct out of ' + str(totalPlayed) + '.') 
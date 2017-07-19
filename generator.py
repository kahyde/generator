import time

from random import SystemRandom
randomGenerator = SystemRandom()

def generateRandomNumber() :
    return randomGenerator.getrandbits(128)

def getCurrentTime() :
    return int(round(time.time()))

def generateId() :
    return "%d-%d" % ( getCurrentTime(), generateRandomNumber() )

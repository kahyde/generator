import generator
import time
from sys import argv

script, num = argv
num = int(num)

startTime = time.time()
idCount = 0

for i in range(0, num) :
    print generator.generateId()
    idCount = idCount + 1

endTime = time.time()
totalTime = endTime - startTime

print "Time: %f seconds, Number of IDs: %d" % ( totalTime, idCount )

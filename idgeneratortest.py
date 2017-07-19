import idgenerator
import time

startTime = time.time()
idCount = 0

for i in range(0, 1000) :
    print idgenerator.generateId()
    idCount = idCount + 1

endTime = time.time()
totalTime = endTime - startTime

print "Time: %f seconds, Number of IDs: %d" % ( totalTime, idCount )

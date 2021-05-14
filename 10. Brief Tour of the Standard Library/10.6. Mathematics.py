import math
print ( math.cos(math.pi / 4) )

print (math.log(1024, 2))

import random
print (random.choice(['apple', 'pear', 'banana']))

print (random.sample(range(100), 10) )  # sampling without replacement

print (random.random()  )  # random float

print (random.randrange(6) )   # random integer chosen from range(6)

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print (statistics.mean(data))

print (statistics.median(data))

statistics.variance(data)
import random
numDigs = 15
numbers = list('0123456789')
random.shuffle(numbers)

secretNum = ''
for i in range(numDigs):
    secretNum += str(numbers[i])

print (secretNum)
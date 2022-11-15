import math, sys
print ('''Factor Finder''')
while True:
    print('Enter a positive whole number to factor (or quit):')
    response = input('> ')
    if response.upper() == 'QUIT' :
        sys.exit()

    if not (response.isdecimal() and int(response)>0):
        continue
    number = int(response)

    factors = []

    #find the factors of number
    for i in range(1, int(math.sqrt(number))+1):
        if number % i == 0: #if there's no remainder, it is  a factor
            factors.append(i)
            factors.append(number//i)

    #get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    for i in range(len(factors)):
        print(factors[i], end = ', ')
    print()


    #for i, factor in enumerate(factors):
        #factors[i]  = str(factor)
    #print (', '.join(factors))
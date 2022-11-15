import datetime, random

def getBirthdays (numbsofbdays):
    birthdays = []
    for i in range(numbsofbdays):
        #get the start of the year
        startOfYear = datetime.date(2001,1,1)
        #get a random day into the year
        randNumberOfDays =  datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """returns the date object of a birthday that occurs more than on in the bday list"""
    if len(birthdays) == len(set(birthdays)):# set is for unique values
        return None #as all are unique --> will not match
    # otherwise, comparing bday to every other bday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA

print ('''Birthday Paradox. The odds that 2 of them have matching birthdays is surprisingly large''')

#set a tuple of month names in order:
Months = ('Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True:
    print('How many birthdays shall I generate? (max 100)')
    response = input ('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break

print ()

#generate and display the bdays:
print('Here are ', numBdays, 'birthdays:')
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma for each bday after the first one
        print (',', end = '')
        monthName = Months[birthday.month -1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print (dateText, end = '')
print()
print()

#See if 2 bdays are matched
match = getMatch(birthdays)

print ('In this simulation, ', end ='')
if match != None:
    monthName =  Months[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
else:
    print ('There are no matching bdays.')
print()


#run 100,000 simulations:
print ('Generating', numBdays, 'random birthdays 100,000 times ...')
input ('Press Enter to begin...')

print ('Let\'s run another 100,000 simulations')
simMatch = 0
for i in range (100_000):
    if i%10_000 == 0:
        print (i, 'simulation run ...')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print ('100,000 sim run.')

probability = round(simMatch/100_000*100,2)
print ('Out of 100,000 sim of ',numBdays, 'people, there was a')
print ('matching birthday in that group ', simMatch, 'times. This means')
print ('that', numBdays, 'people have a ', probability, '% chance of')
print ('having a matching bday in their group.')
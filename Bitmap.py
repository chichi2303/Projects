import sys

bitmap = '''
test test test test moreofthetest 
if this is ok
'''
print ('Bitmap Message')
print ('Enter the message to display with the bitmap.')
message = input ('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for i in range(len(line)):
        if line[i] ==' ':
            print (' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()




#loop over each line in the bitmap
    #loop over each char in the line
#for line in bitmap.splitlines():
#    for i, bit in enumerate(line):
#        if bit ==' ':
#            print (' ', end ='')
#        else:
#            print(message[i % len(message)], end='')
#    print()
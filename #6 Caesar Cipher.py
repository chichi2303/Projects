try:
    import pyperclip
except ImportError:
    pass

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print ('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print ('Please enter the letter e or d')

#let user enters the key to use:
while True:
    maxKey = len(symbols) -1
    print ('please enter the key (0 to {}) to use.'.format(maxKey))
    responseKey = input('> ').upper()
    if not responseKey.isdecimal():
        continue
    if 0 <= int(responseKey) < len(symbols):
        key = int(responseKey)
        break

print ('Enter the message to {}'.format(mode))
message = input ('> ')
message = message.upper()

translated = ''

for symbol in message:
    if symbol in symbols:
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode =='decrypt':
            num = num - key

        #handle the wrap0-around if num is larger than the length of symbols or less than 0
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)

        #add encrypted/decrypted number's symbol to translate:
        translated = translated + symbols[num]

    else:
        #just add the symbol without encrypting/decrypting:
        translated = translated + symbol

print (translated)

try:
    pyperclip.copy(translated)
    print ('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass

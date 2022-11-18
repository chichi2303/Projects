print ('Enter the encrypted Caesar cipher message to hack.')
message = input ('> ')

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(symbols)):
    translated = ''

    for symbol in message:
        if symbol in symbols:
             num = symbols.find(symbol)
             num = num - key

             if num < 0:
                num = num + len(symbols)
             translated = translated + symbols[num]
        else:
            translated = translated + symbol


    print ('Key #{}: {}'.format(key,translated))
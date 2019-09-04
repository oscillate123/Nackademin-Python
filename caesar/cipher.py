SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"#€%&/()=?<>'
MAX_KEY_SIZE = len(SYMBOLS)
MODES = ['encrypt', 'e', 'decrypt', 'd']


def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in MODES:
            return mode
        elif mode == "no":
            print('Ok, good bye "Brutus".')
            exit()
        else:
            print(f'Enter either "{MODES[0]}" or "{MODES[1]}" or "{MODES[2]}" or "{MODES[3]}".')


def getMessage():
    print('Enter your message:')
    user_input = input()
    list_user_input = list(user_input)
    list_user_input.reverse()
    user_input = list_user_input
    return user_input
    # receives user input and reverse it


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % MAX_KEY_SIZE)
        key = int(input())
        if MAX_KEY_SIZE >= key >= 1:
            return key


def getTranslatedMessage(mode, message, key):

    translated = ''

    if mode[0] == 'd':
        key = -key

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Symbol not found in SYMBOLS.
            # Just add this symbol without any change
            translated += symbol
        else:
            # Encrypt or decrypt
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated


mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))

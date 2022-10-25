
'''
24 - Movie Quotes To Clipboard - V1
- In command in the program`s folder, the format:
        py name of the program(24_chptr6_MovieQuotesToClipboard_V1) keyphrase(like zoo, fish..)

- The program will copy the value of the keyphrase to clipboard.
'''

text = { 'zoo': "I've had it with these motherfucking snakes on this motherfucking plane!",
        'fish': "You're gonna need a bigger boat.",
        'coffee': "I love the smell of napalm in the morning.",
        'fragile': "You can't handle the truth!",
        'mobile': "E.T. phone home.",
        'cemetery': "I see dead people.",
        'midget': "Say 'hello' to my little friend!",
        'toitoi': "I'm the king of the world!",
        'hangover': "Toto, I`ve a feeling we`re not in Kansas anymore."}

import sys, pyperclip as pc

if len(sys.argv) < 2:
        print()
        print('The correct format: py + program name + keyphrase')
        sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
        pc.copy(text[keyphrase])
        print()
        print('The quote copied to clipboard.')
else:
        print('Wrong keyphrase.')


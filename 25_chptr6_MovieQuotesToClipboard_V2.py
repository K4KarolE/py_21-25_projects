
'''
25 - Movie Quotes To Clipboard - V2 - Chapter 6 - Practice
- ask the user for a keyword or list of the keywords or quite
- the movie quote belongs to the keyword will be displayed and copied to the clipboard
'''

text = { 'zoo': "I've had it with these motherfucking snakes on this motherfucking plane!",
        'fishy': "You're gonna need a bigger boat.",
        'coffee': "I love the smell of napalm in the morning.",
        'fragile': "You can't handle the truth!",
        'mobile': "E.T. phone home.",
        'cemetery': "I see dead people.",
        'midget': "Say 'hello' to my little friend!",
        'toitoi': "I'm the king of the world!",
        'hangover': "Toto, I`ve a feeling we`re not in Kansas anymore."}

import sys, pyperclip as pc

print()
while True:
        print()
        answer = input('Add keyword to copy the related quote to the clipboard or type\n`Q` for quit\n`L` to list the current keywords: ').lower()
        if answer == 'q':
                print()
                print('Thx for checking in!')
                print()
                sys.exit()

        elif answer == 'l':
                print()
                keyList = list(text.keys())
                keyList.sort()
                for i in keyList:
                        print(i)
        elif answer in text.keys():
                print()
                pc.copy(text[answer])
                print('The quote copied to the clipboard: ')
                print(text[answer].rjust(len('The quote copied to the clipboard:') + len(text[answer])))
                print()
        else:   
                print()
                print('No such keyword in our database. Try again.')
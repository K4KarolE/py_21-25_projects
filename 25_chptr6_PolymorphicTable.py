'''
25 - Polymorphic Table - Chapter 6 - Practice
- ask the user for the number of words should be displayed
- ask the user for the number of columns should we use
- create a list for every column
- find the longest word/item in every column, it`s length will be the width of that column
'''

import sys

while True:
    try:
# USER INPUT - AMOUNT OF WORDS AND COLUMNS
        print()
        print('- POLYMORPHIC TABLE -'.center(len('How many words should we display(1-100):'+' '*3),'-'))
        items = input('How many words should we display(1-100): ')
        while items.isdigit() == False or int(items) <1 or int(items) > 100:
            print()
            print('Your answer should be a number between 1 and 100.')
            items = input('How many words should we display(1-100): ')
        items = int(items)

        columnNumber = input('In how many columns: ')
        while columnNumber.isdigit() == False or int(columnNumber) < 1:
            print()
            print('Your answer should be a positive number.')
            columnNumber = input('In how many columns: ')
        columnNumber = int(columnNumber)

# PICK THE WORDS FROM FILE
        file = open(r'25_chptr6_100_random_words.txt','r+')
        fileList = list(file)
        file.close()

        table = []
        for i in range(items):
            table.append(fileList[i].strip('\n').strip())   # removing the `\n` and the extra spaces from the items

        tableLength = len(table)
        averageColumnLength = int(tableLength / columnNumber)
        mod = tableLength % columnNumber        # if the tableLength/columnNumber not integer
        print()                                 # we would add an extra item to the lists, starting with the 1st list
                                                # example: 24 items in the chosen list, in 5 columns: we should place 1 extra item in the first 4 columns


# NUMBER OF COLUMNS < NUMBER OF ITEMS
# CREATING LISTS
        tableList = []
        columnWidth = []
        tableWidth = 0               
        for i in range(columnNumber):       
                tableList.append([])        # creating list for every column
                columnWidth.append([0])      # creating list for every column`s width

        if columnNumber < tableLength:
            for i in range(columnNumber):
                for p in range(averageColumnLength):
                    tableList[i].append(table[averageColumnLength*i+p])
                if mod > 0:                                               
                    tableList[i].append(table[averageColumnLength*i+p+1])   # adding an extra item to the list
                    del table[averageColumnLength*i+p+1]    # removing this extra item from the original/chosen list, so the next list will not include this item
                    mod -= 1

# FINDING THE WIDTH OF EVERY COLUMN   
            for i in range(columnNumber):
                for p in range(len(tableList[i])):
                    if len(tableList[i][p]) > columnWidth[i][0]:
                        columnWidth[i][0] = len(tableList[i][p])
                tableWidth = tableWidth + columnWidth[i][0] + 2      # we will use this value to print the table title banner

## PRINTING ##
# NUMBER OF COLUMNS = 1
        if columnNumber == 1:
            print('- YOUR TABLE -'.center(columnWidth[i][0],'-'))
            tableList = tableList[0]
            for item in tableList:
                print(item.rjust(columnWidth[i][0]))

# NUMBER OF COLUMNS > 1
        maxListLength = len(tableList[0])   # because we moved one of the "modulo" items into the 1st list (if there was any, like: 21 items in 5 columns)
                                            # this list`s` length will be the maximum(or equal to other +modulo items list`s length, like: 24 items in 5 columns)
        if columnNumber > 1 and columnNumber < tableLength:
            print('- YOUR TABLE -'.center(tableWidth,'-'))
            for g in range(maxListLength):
                for k in range(columnNumber):
                    if g in range(len(tableList[k])):   # making sure there is no "out of index error" like: 21items/5columns -> 1st list`s length:5 / 2nd list`s length:4
                        print(tableList[k][g].rjust(columnWidth[k][0]), end = '  ')       
                print()

# NUMBER OF COLUMNS > NUMBER OF ITEMS
        if columnNumber >= tableLength:
            for i in range(len(table)):
                tableWidth = tableWidth + len(table[i]) + 1
            print('- YOUR TABLE -'.center(tableWidth,'-'))
            for i in table:
                print(i, end=' ')
            print()
        print()
    except KeyboardInterrupt:
        print('\n')
        print('Thx for stopping by!\n')
        sys.exit()
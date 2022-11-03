
'''
25 - Polymorphic Table - Chapter 6 - Practice
- ask the user for the number of words should be displayed (1-100)
- ask the user for the number of columns should we use
- create a list for every column
- find the longest word/item in every column, it`s length will be the width of that column
'''


# - ask for the number of words should be displayed (1-100)
# - ask for the number of columns

table = ['zoo','fishy','coffee','fragile','mobile','cemetery','midget','toitoi','hangover']   # 9

columnNumber = 1

tableLength = len(table)

averageColumnLength = int(tableLength / columnNumber)
mod = tableLength % columnNumber           # if the tableLength/columnNumber not integer
                                           # we would add an extra item to the lists, starting with the 1st list
                                           # example: 24 items in the chosen list, in 5 columns: we should place 1 extra item in the first 4 columns
print()



# NUMBER OF COLUMNS < NUMBER OF ITEMS
# CREATING LISTS
tableList = []
columnWidth = []
tabletWidth = 0               
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
        tabletWidth = tabletWidth + columnWidth[i][0] + 2      # we will use this value to print the table title banner

# PRINTING
# COLUMNS NUMBER = 1
if columnNumber == 1:
    print('- YOUR TABLE -'.center(columnWidth[i][0],'-'))
    tableList = tableList[0]
    for item in tableList:
        print(item.rjust(columnWidth[i][0]))

# COLUMNS NUMBER > 1
maxListLength = len(tableList[0])   # because we moved one of the "modulo" items into the 1st list (if there was any, like: 21 items in 5 columns)
                                    # this list`s` length will be the maximum(or equal to other +modulo items list`s length, like: 24 items in 5 columns)
if columnNumber > 1 and columnNumber < tableLength:
    print('- YOUR TABLE -'.center(tabletWidth,'-'))
    for g in range(maxListLength):
        for k in range(columnNumber):
            if g in range(len(tableList[k])):   # making sure there is no "out of index error" like: 21items/5columns -> 1st list`s length:5 / 2nd list`s length:4
                print(tableList[k][g].rjust(columnWidth[k][0]), end = '  ')
        
        print()


# NUMBER OF COLUMNS > NUMBER OF ITEMS
if columnNumber >= tableLength:
    for i in range(len(table)):
        tabletWidth = tabletWidth + len(table[i]) + 1
    print('- YOUR TABLE -'.center(tabletWidth,'-'))
    for i in table:
        print(i, end=' ')
    print()


print()


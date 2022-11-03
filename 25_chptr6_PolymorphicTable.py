
'''
25 - Polymorphic Table - Chapter 6 - Practice
- ask for the number of words should be displayed (1-100)
- ask for the number of columns
- determine how many items will be in 1/each column
- determine the longest word in every column, that will be the width of that column
'''


# - ask for the number of words should be displayed (1-100)
# - ask for the number of columns

table = ['zoo','fishy','coffee','fragile','mobile','cemetery','midget','toitoi','hangover']   # 9

columnNumber = 3
tableLength = len(table)

averageColumnLength = int(tableLength / columnNumber)
mod = tableLength % columnNumber           # if the tableLength/columnNumber not integer
                                           # we would add an extra item to the lists, starting with the 1st list
                                           # example: 24 items in the chosen list, in 5 columns: we should place 1 extra item in the first 4 column

print()
if columnNumber >= tableLength:
    for i in table:
        print(i, end=' ')
print('\n')

print()



# CREATING LISTS
tableList = []
columnWidth = []                  
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

# PRINTING THE COLUMNS / TABLE
    for p in range(len(tableList[p])):
        for i in range(columnNumber):
            print(tableList[i][p].rjust(columnWidth[i][0]), end = '   ')
        print()

                
    








# print(columnWidth)
# print(tableList)
print()

# FINDING THE LONGEST ITEM IN THE LISTS/COLUMNS

    






# print(averageColumnLength)
# print(tableLength)
# print(mod)


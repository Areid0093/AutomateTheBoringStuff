## Table Printer
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    ## Iterate over each column in data with for col in data
    ## Retrieve the longest item in each column with max using key=len
    ## Add the length of that longest item to the list using len
    colWidth = [len(max(col, key=len)) for col in data]
    
    ## Iterate over data, printing the x value from each inner list
    ## right justify each printed x value according to its value in colWidths
    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(colWidth[y]), end = ' ')
        print('')
        
printTable(tableData)

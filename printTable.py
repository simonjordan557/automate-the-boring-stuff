#! /usr/bin/python3

# printTable.py - Displays a list of lists of strings in a justified table.

tableData = [['bacon', 'eggs', 'spam', 'sausage'], ['apples', 'oranges', 'cherries', 'bananas'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'mice', 'moose']]

colWidths = [0] * len(tableData)    # Create a list(int) of the longest string in each column.
for i in range(len(colWidths)):
    for j in range(len(tableData[i])):
        width = len(tableData[i][j])
        if width > colWidths[i]:
            colWidths[i] = width

for j in range(len(tableData[0])):
    print('\n')
    for i in range(len(tableData)):
       print(tableData[i][j].rjust(colWidths[i]), end = ' ') 
    
        

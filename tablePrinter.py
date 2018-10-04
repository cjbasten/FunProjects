def printTable(table):
    colWidths = [0] * len(table)
    for k in range(len(table)):
        for v in table[k]:
            if len(v) > colWidths[k]:
                colWidths[k] = len(v)

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), end=' ')
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

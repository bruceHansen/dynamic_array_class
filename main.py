import csv
import inspect
from arrays import Array

datacsv = open('data.csv')
datareader = csv.reader(datacsv, delimiter=' ')

line_number = 0
my_commands = []

csvfile = open('output.txt', 'w', newline='')

datawriter = csv.writer(csvfile, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)

for line in datareader:

    datawriter.writerow(['{}:{}'.format(line_number, line[0])])
    line_number += 1
    my_commands.append(line[0])

    #check which command is called

    if line[0].strip().split(',')[0] == 'CREATE':
        ar = Array()

    elif line[0].strip().split(',')[0] == 'ADD':
        ar.add(line[0].strip().split(',')[1])

    elif line[0].strip().split(',')[0] == 'GET':
        datawriter.writerow([ar.get(line[0].strip().split(',')[1])])

    elif line[0].strip().split(',')[0] == 'DELETE':
        if ar.delete(line[0].strip().split(',')[1]):
            datawriter.writerow([ar.delete(line[0].strip().split(',')[1])])

    elif line[0].strip().split(',')[0] == 'SWAP':
        if ar.swap(line[0].strip().split(',')[1], line[0].strip().split(',')[2]):
            datawriter.writerow([ar.swap(line[0].strip().split(',')[1], line[0].strip().split(',')[2])])

    elif line[0].strip().split(',')[0] == 'SET':
        if ar.set(line[0].strip().split(',')[1], line[0].strip().split(',')[2]):
            datawriter.writerow([ar.set(line[0].strip().split(',')[1], line[0].strip().split(',')[2])])

    elif line[0].strip().split(',')[0] == 'INSERT':
        if ar.insert(line[0].strip().split(',')[1], line[0].strip().split(',')[2]):
            datawriter.writerow([ar.insert(line[0].strip().split(',')[1], line[0].strip().split(',')[2])])

    elif line[0].strip().split(',')[0] == 'DEBUG':
        datawriter.writerow([ar.debug_print()])

    else:
        datawriter.writerow(['no command found'])

	
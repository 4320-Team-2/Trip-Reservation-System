#need to create a list containing 12 lists each of 4 items, all set to 0

import numpy as np
import csv 


seat_chart = np.full((12, 4,), 'O', dtype=str)

#Sets seat in row 3 seat 3 to the numnber 0
#neeed to do this for every requirement
reserv_read = open("it-4320-final-proj/reservations.txt", "rt")
reserv_data = reserv_read.read()
reserv_read.close



seat_chart[2,2] = 8



with open ('it-4320-final-proj/reservations.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #row = row[1]
        #rowint = int(row)
        #column = row[2]
        #columnint = int(column)
        seat_chart[int(row[1]), int(row[2])] = 'X'
        #print(f'\t {row[1]},{row[2]}')
        line_count += 1


print(seat_chart)

if seat_chart[2,3] == "O":
    print("seat available")
else:
    print("seat taken")
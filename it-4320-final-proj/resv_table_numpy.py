#need to create a list containing 12 lists each of 4 items, all set to 0

import numpy as np
import csv

def createChart():

    seat_chart = np.full((12, 4,), 'O', dtype=str)

    #Sets seat in row 3 seat 3 to the numnber 0
    #neeed to do this for every requirement
    reserv_read = open("reservations.txt", "rt")
    reserv_data = reserv_read.read()
    reserv_read.close

    with open ('reservations.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            seat_chart[int(row[1]), int(row[2])] = 'X'
            line_count += 1


    return seat_chart

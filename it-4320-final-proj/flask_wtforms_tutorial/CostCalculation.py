#Function takes seating matrix as parameter returns revenue amount
#seatMatrix = [["O","O","O","O"] for row in range(12)]
#seatMatrix[3][2] = "X"

def costCalculation(seatMatrix):
#Matrix for determing seating cost
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    revenue = 0
#Iterates through the seating matrix and for every "X" encountered, adds the corresponding cost matrix to the revenue value.
    for k in range(4):
        for j in range(12):
            if seatMatrix[j][k] == "X":
                revenue += cost_matrix[j][k]
                
    return revenue

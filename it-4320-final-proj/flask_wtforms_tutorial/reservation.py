from pathlib import Path
def addRes(fname, row, col, ticketNum):
    path = Path(__file__).parent / "../reservations.txt"
    with path.open("a") as f:
        name = fname + ", "
        row = str(row) + ", "
        col = str(col) + ", "
        ticketNum = ticketNum + "\n"
        f.write(name + row + col + ticketNum)
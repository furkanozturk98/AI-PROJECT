# f = open("sudokus_start.txt", "r")
import sys
from BTS import BTS
l = []
"""
for i in f:
    counter = 1
    for j in i:
        if(counter <= 9):
            print(j,end=" ")
            counter = counter +1
        else:
            print()
            counter = 2
            print(j,end=" ")"""

"""
for i in f:
    counter = 1
    TepList=[]
    for j in i:
        if(counter <= 9):
            TepList.append(int(j))
            counter = counter +1
        else:
            l.append(TepList.copy())
            TepList.clear()
            TepList.append(int(j))
            counter = 2
    l.append(TepList.copy())
f.close()"""


def readFile():
    #f = open("sudokus_start.txt", 'r').read().split('\n')
    with open(sys.argv[1], 'r') as f:
        sudokus = []
        for i in f:
            i = i.rstrip('\n')
            sudokus.append(i)
    return sudokus


def readSudoku(index):
    sudokus = readFile()
    
    counter = 1
    TepList = []
    for j in sudokus[index]:
        if(counter <= 9):
            TepList.append(int(j))
            counter = counter + 1
        else:
            l.append(TepList.copy())
            TepList.clear()
            TepList.append(int(j))
            counter = 2
    l.append(TepList.copy())
    return l

"""
board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:  # if find is None or False
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                print(bo[i][j], " ┃")
            else:
                print(bo[i][j], end=" ")

    print(" ┖─────────┸─────────┸─────────┚")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column

    return None
"""

def main():

    bts = BTS()
    l = readSudoku(2)
    bts.print_board(l)
    print('\n--------------------------------------\n')
    print(bts.solve(l))
    bts.print_board(l)






if __name__ == '__main__':
    main()

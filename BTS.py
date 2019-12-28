 
class BTS:

    def find_empty(self,bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return i, j  # row, column

        return None

    def valid(self,bo, num, pos):

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

    def solve(self,sudoku):
        bo = sudoku.getSudoku()
        find = self.find_empty(bo)
        if not find:  # if find is None or False
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.valid(bo, num, (row, col)):
                bo[row][col] = num

                if self.solve(sudoku):
                    return True

            bo[row][col] = 0

        return False

    

    def print_board(self,sudoku):
        bo = sudoku.getSudoku()

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


    

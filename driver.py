import sys
from BTS import BTS
import time
from SudokuGenerator import SudokuGenerator
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from sudoku import Sudoku
from ac3 import AC3
from backtrack import recursive_backtrack_algorithm



class driver:

    sudokuList = []
    bts = BTS()
    N = 9
    K = 55
    sudoku = SudokuGenerator(N,K)
    sudoku.fillValues()


    my_window = tk.Tk()
    my_window.geometry('430x500')
    canvas = tk.Canvas(my_window, width = 360, height = 360, bg = "white")
    canvas.pack(side = "top")
    labels = {}
    button1 = None
    button2 = None
    combo = None
    textBox1 = None

    def paint(self,sudoku):
        
        sudokuList = sudoku.getSudoku()

        coloredBoxes = [
            (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),
            (0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8),
            (3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5),
            (6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),
            (6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8),
                        ]

        for i in range(9):
            TempList = []
            mylabel = None
            for j in range(9): 
                
                if (i,j) in coloredBoxes :
                    self.canvas.create_rectangle(0+(j*40),0+(i*40),40+(j*40), 40+(i*40),fill="turquoise")
                    mylabel = self.canvas.create_text(0+(j*30),0+(i*30),fill="black",font="Times 10",text="")
              
              
                self.canvas.create_rectangle(0+(j*40),0+(i*40),40+(j*40), 40+(i*40))
                mylabel = self.canvas.create_text(20+(j*40),20+(i*40), fill="black",font="Times 13",text="") 

                TempList.append(mylabel)
            self.labels[i] = TempList    
        
        
        

        for i in range(9):
            for j in range(9):
                if sudokuList[i][j] != 0:
                    self.canvas.itemconfig(self.labels[i][j], text = sudokuList[i][j] )

        self.canvas.grid(padx=30,pady=10)

        self.button1 = tk.Button(self.my_window, command= lambda: self.solveButtonClick(sudoku) ,text = "Solve",height = 3, width = 10)
        self.button2 = tk.Button(self.my_window, command= self.refreshButtonClick ,text = "Refresh",height = 3, width = 10)
        content=["","AC3","Backtracking","Heuristic Backtracking"]

        self.combo = Combobox(self.my_window,values=content)

        self.textBox1 = tk.Entry(self.my_window)
        label = tk.Label(self.my_window, text = "Number of empty cells:")

        self.button1.place(x=200,y=400)
        self.button2.place(x=300,y=400)
        self.combo.place(x=40,y=405)
        label.place(x=40,y=440)
        self.textBox1.place(x=40,y=460)

        
        self.my_window.mainloop()

    def refreshButtonClick(self):
        K = None
        if self.textBox1.get() != "" and str.isdigit(self.textBox1.get()) :
            if int(self.textBox1.get()) > 0 and int(self.textBox1.get()) < 80:
                K = self.textBox1.get()
                
            else:
                K = self.K
              
        else:
            K = self.K
          

        self.sudoku = SudokuGenerator(self.N,int(K))
        self.sudoku.fillValues()
        self.bts.print_board(self.sudoku.getSudoku())

        sudokuList = self.sudoku.getSudoku()
        for i in range(9):
            for j in range(9):
                if sudokuList[i][j] != 0:
                    self.canvas.itemconfig(self.labels[i][j], text = sudokuList[i][j]  )
                else:
                    self.canvas.itemconfig(self.labels[i][j], text = ""  )

        self.button1.config(state="normal")


    def solveButtonClick(self,sudoku):
        
        if self.combo.get() == "":
            tk.messagebox.showwarning("", "Please select an algorithm.")


        if self.combo.get() == "Backtracking":

            sudokuList = sudoku.getSudoku()

            print('\n--------------------------------------\n')
            start = time.time()
            self.bts.solve(sudokuList)
            self.bts.print_board(sudokuList)

            for i in range(9):
                for j in range(9):
                    self.canvas.itemconfig(self.labels[i][j], text = sudokuList[i][j]  )
        
            print ("Time: ", round(time.time() - start,2), "seconds.")
            self.button1.config(state="disabled")
            tk.messagebox.showinfo("Execution Time", str(round(time.time() - start,2)) + " seconds.")
        

        if self.combo.get() == "AC3":
            grid = self.sudoku.getSudokuAsString()
            sudoku = Sudoku(grid)
            start = time.time()
            AC3_result = AC3(sudoku)
            if not AC3_result:
                print("this sudoku has no solution")
                tk.messagebox.showerror("this sudoku has no solution")
            else:
                if sudoku.isFinished():
                    print("AC3 was enough to solve this sudoku !")
                    executionTime = round(time.time() - start,2)
                    print ("Time: ", executionTime , "seconds.")
                    self.bts.print_board(sudoku.sudokuAsMatrix())
                    
                    for i in range(9):
                        for j in range(9):
                            self.canvas.itemconfig(self.labels[i][j], text = sudoku.sudokuAsMatrix()[i][j]  )

                    tk.messagebox.showinfo("Execution Time", str(executionTime) + " seconds.")
                    self.button1.config(state="disabled")
                else:
                    print("AC3 was not enough to solve this sudoku !")
                    tk.messagebox.showerror("","AC3 was not enough to solve this sudoku !")
                    self.refreshButtonClick()

        
        if self.combo.get() == "Heuristic Backtracking":
            grid = self.sudoku.getSudokuAsString()
            sudoku = Sudoku(grid)
            print("Heuristic Backtracking starting...")

            assignment = {}

            start = time.time()

            # start backtracking
            assignment = recursive_backtrack_algorithm(assignment, sudoku)
            
            # merge the computed values for the cells at one place
            for cell in sudoku.possibilities:
                sudoku.possibilities[cell] = assignment[cell] if len(cell) > 1 else sudoku.possibilities[cell]

            if assignment:
                print("Result:")
                executionTime = round(time.time() - start,2)
                print ("Time: ", executionTime , "seconds.")
                self.bts.print_board(sudoku.sudokuAsMatrix())

                for i in range(9):
                    for j in range(9):
                        self.canvas.itemconfig(self.labels[i][j], text = sudoku.sudokuAsMatrix()[i][j]  )

                tk.messagebox.showinfo("Execution Time", str(executionTime) + " seconds.")
                self.button1.config(state="disabled")
                




    def main(self):
    

        self.bts.print_board(self.sudoku.getSudoku())

        self.paint(self.sudoku) 
        
        
        


driver = driver()
driver.main()

import sys
from BTS import BTS
import time
from SudokuGenerator import SudokuGenerator
import tkinter as tk
from tkinter import messagebox
class driver:

    sudokuList = []
    bts = BTS()
    N = 9
    K = 55
    sudoku = SudokuGenerator(N,K)
    sudoku.fillValues()

    def readFile(self):
        with open(sys.argv[1], 'r') as f:
            sudokus = []
            for i in f:
                i = i.rstrip('\n')
                sudokus.append(i)
        return sudokus


    def readSudoku(self,index):
        sudokus = self.readFile()
    
        counter = 1
        TempList = []
        for j in sudokus[index]:
            if(counter <= 9):
                TempList.append(int(j))
                counter = counter + 1
            else:
                self.sudokuList.append(TempList.copy())
                TempList.clear()
                TempList.append(int(j))
                counter = 2
        self.sudokuList.append(TempList.copy())
        return self.sudokuList

    my_window = tk.Tk()
    my_window.geometry('430x500')
    canvas = tk.Canvas(my_window, width = 360, height = 360, bg = "white")
    canvas.pack(side = "top")
    labels = {}
    button1 = None
    button2 = None
    

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
            
                self.canvas.itemconfig(self.labels[i][j], text = sudokuList[i][j] )

        self.canvas.grid(padx=30,pady=10)

        self.button1 = tk.Button(self.my_window, command= lambda: self.buttonClick(sudoku) ,text = "Solve",height = 3, width = 10)
        self.button2 = tk.Button(self.my_window, command= self.refreshbuttonClick ,text = "Refresh",height = 3, width = 10)
        self.button1.place(x=120,y=400)
        self.button2.place(x=220,y=400)
        
        self.my_window.mainloop()

    def refreshbuttonClick(self):
        print("hello")
        self.sudoku = SudokuGenerator(self.N,self.K)
        self.sudoku.fillValues()
        self.bts.print_board(self.sudoku)

        sudokuList = self.sudoku.getSudoku()
        for i in range(9):
            for j in range(9):
            
                self.canvas.itemconfig(self.labels[i][j], text = sudokuList[i][j]  )

        self.button1.config(state="normal")


    def buttonClick(self,sudoku):
        
        sudokuList = sudoku.getSudoku()

        print('\n--------------------------------------\n')
        start = time.time()
        self.bts.solve(self.sudoku)

        self.bts.print_board(self.sudoku)

        for i in range(9):
            for j in range(9):
            
                self.canvas.itemconfig(self.labels[i][j], text = sudokuList[i][j]  )
        
        print ("Time: ", round(time.time() - start,2), "seconds.")

        self.button1.config(state="disabled")

        tk.messagebox.showinfo("Execution Time", str(round(time.time() - start,2)) + " seconds.")


    def main(self):
    
        #sudokuList = readSudoku(1)


        self.bts.print_board(self.sudoku)
        self.paint(self.sudoku)

        
        
        


driver = driver()
driver.main()

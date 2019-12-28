import math
import random
import time
class SudokuGenerator():
    N = 0
    K = 0
    SRN = 0
    mat = [0] * 9
    def __init__(self,N,K):
        self.N = N
        self.K = K

        SRNd = math.sqrt(N)
        self.SRN = int(SRNd)
        


        for i in range(N):
            self.mat[i] = [0] * 9

    def fillValues(self):
        # Fill the diagonal of SRN x SRN matrices 
        self.fillDiagonal()
        
        # Fill remaining blocks 
        self.fillRemaining(0, self.SRN)
  
        # Remove Randomly K digits to make game 
        self.removeKDigits()

    def fillDiagonal(self):
        
        i=0
        while(i < self.N):
            self.fillBox(i, i)
            i = i + self.SRN

    def unUsedInBox(self,rowStart,colStart,num): 
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[rowStart+i][colStart+j] == num:
                    return False
  
        return True

    def fillBox(self,row,col):
        num = 0
        for i in range(self.SRN):
            for j in range(self.SRN):
               
                num = self.randomGenerator(self.N)
                while (self.unUsedInBox(row, col, num) == False):
                    num = self.randomGenerator(self.N)
  
                self.mat[row+i][col+j] = num

    def randomGenerator(self,num):
        return int(math.floor((random.random()*num+1)))
    
    def CheckIfSafe(self,i,j,num):

        

        return (self.unUsedInRow(i, num) and 
                self.unUsedInCol(j, num) and 
                self.unUsedInBox(i-i%self.SRN, j-j%self.SRN, num))
    
    def unUsedInRow(self,i,num):

        for j in range(self.N):
           if (self.mat[i][j] == num):
                return False
        return True
 
   
    def unUsedInCol(self,j,num):

        for i in range(self.N): 
            if (self.mat[i][j] == num):
                return False 
        return True

    def fillRemaining(self,i,j):
        #print(i,j , self.N)
        

        if (j >= self.N and i < self.N-1):
            i = i + 1
            j = 0

        if (i >= self.N and j >= self.N):
            return True
  
        if (i < self.SRN):
            if (j < self.SRN):
                j = self.SRN

        elif (i < self.N - self.SRN):

            if (j == int((i/self.SRN))*self.SRN):
                j =  j + self.SRN

        else:
            if (j == self.N - self.SRN):
                i = i + 1
                j = 0
                if (i >= self.N):
                    return True

        for num in range(1,self.N + 1):
            if (self.CheckIfSafe(i, j, num)):

                self.mat[i][j] = num
                if (self.fillRemaining(i, j+1)):
                    return True
  
                self.mat[i][j] = 0


        return False

    def removeKDigits(self):

        count = self.K
        while (count != 0):

            cellId = self.randomGenerator(self.N*self.N)
  
            
            i = int(cellId/self.N) 
            j = int(cellId%9)
            if (j != 0):
                j = j - 1
  
            try:
                if (self.mat[i][j] != 0):
            
                    count = count - 1
                    self.mat[i][j] = 0
            except:
                print("")

    def printSudoku(self): 

        for i in range(self.N):

            for j in range(self.N):
                print(self.mat[i][j]," ",end="")
            print()

    def getSudoku(self):
        return self.mat






         
    



    
    
    
            
        
    
     
    
    

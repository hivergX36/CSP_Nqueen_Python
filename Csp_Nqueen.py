import re 
import numpy as np

class CspNqueens:
    
    def __init__(self,n: int) -> None:
        self.nbrow = n
        self.nbcol = n
        self.board = [0 for i in range(n)]
        self.compteur = 0 
        
    
    def set_value(self,row,val):
        self.board[row] = val
        
 
        
    def check_constraint(self,row,val):
        for i in range(row):
            if self.board[i] == val or abs(self.board[i] - val) == abs(i - row):
                return False
        return True



    
    def AC3_solve(self):
        for i in range(0,self.nbrow):
            if self.board[i] == 0:
                for j in range(1,self.nbcol + 1):
                    if self.check_constraint(i,j):
                        self.set_value(i,j)
                        if self.AC3_solve():
                            return True
                        self.set_value(i,0)
                return
        print(self.board)
                    
        
    
    
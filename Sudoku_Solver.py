import numpy as np
import pandas as pd

dataset = pd.read_csv("Sudoku_grid.txt",delimiter='\t',header=None)
grid = dataset.iloc[:,:].values
#print(np.matrix(grid))
call=0

def Check(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n:
            return False
    X = (x//3)*3
    Y = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[Y+i][X+j]==n:
              return False
    return True

def solve():
    
    global grid,call
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x]==0:
                for n in range(0,10):
                     if Check(y,x,n):
                         grid[y][x]=n
                         solve()
                         call+=1
                         grid[y][x]=0
                
                return  
                    
        
                
    print("no.of Recursion:",call)    
    print(np.matrix(grid))
    exit(0)

solve()







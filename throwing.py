import numpy as np
# m: number of floors, n: number of eggs 
def MaxCost(m,n):
# generating a two-dimensional array
   C = np.zeros((m+1, n+1), dtype=np.int)         
   
   for i in range(1,n+1):
       C[1][i] = 15
   
   for j in range(0, m+1 ):
       if (j==0):
           C[j][1]=0
       else:
           C[j][1] = j * 10 + 5
   
   for x in range(2, n +1):
       for y in range(2, m +1):
           for z in range(1, y +1):
               if (z == 1):
                # initial value
                   C[y][x] = 10 + max(C[z - 1][x - 1] + 5, C[y - z][x])    
               else:
                   C[y][x] = min(C[y][x], (10 + max(C[z - 1][x - 1] + 5, C[y - z][x])))
   print(C)
   print("The mininum cost is :",C[y][x])

if __name__=='__main__':
	M=int(input("please enter eggNum\n"))
	N=int(input("please enter floorNum\n"))
	MaxCost(M,N)

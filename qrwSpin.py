from numpy import *
import matplotlib.pyplot as plt

size = 101
N = 60
v=sqrt(0.5)
center = int(round((size - 1) / 2))
Psi = full((size,2),0.j)
H = v * array([[1,1],[1,-1]])
Psi[center] = v * array([1,1j])
listPsi = [Psi]

for j in range(N):
      oldPsi=listPsi[-1]
      coinflipPsi = [matmul(H,x) for x in oldPsi]
      newPsi = full((size,2),0.j)
      for i in range(1,size-1):           
            newPsi[i] =[ coinflipPsi[i+1][0],coinflipPsi[i-1][1]] 
               
      listPsi.append(newPsi)
      
plt.plot([abs(x[0])**2 + abs(x[1])**2 for x in listPsi[-1] ])
plt.show()
      

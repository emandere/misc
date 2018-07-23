from numpy import *
import matplotlib.pyplot as plt
def fillTuple(size,vals):
      listval=[]
      for i in range(size):
            listval.append(vals)
      return listval

size = 101
center = int(round((size - 1) / 2))
Psi = fillTuple(size,[0.,0.])
P = full(size,0.)
N = 60
v=sqrt(0.5)
H = v * array([[1,1],[1,-1]])
P[center] = 1.0
Psi[center] = v * array([1,1j])
listP=[P]
listPsi = [Psi]
#print(Psi)
for j in range(N):
      oldPsi=listPsi[-1]
      oldP=listP[-1]
      shiftPsi = [matmul(H,x) for x in oldPsi]
      #print(shiftPsi)
      newPsi = fillTuple(size,[0.,0.])
      newP = full(size,0.)
      for i in range(1,size-1):
            x=[0,0]
            x[0]=shiftPsi[i+1][0]
            x[1]=shiftPsi[i-1][1]
            newPsi[i]=x            
            newP[i] =  abs(x[0])**2 + abs(x[1])**2     
            
      listPsi.append(newPsi)
      listP.append(newP)
      print(listP[-1])
      #print(listPsi[-1])
      
plt.plot(listP[-1])
plt.show()
      

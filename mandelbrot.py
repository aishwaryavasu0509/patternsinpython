import numpy
from numba import jit
import matplotlib.pyplot as plt
@jit
def mandelbrot(Re,Im,max_iter):
    c=complex(Re,Im)
    z=0.0j
    for i in range(max_iter):
        z=z*z+c
        if(z.real*z.real+z.imag*z.imag)>=4:
            return i
    return max_iter
coloumns=2000
rows=2000
result=numpy.zeros([rows,coloumns])
for row_index,Re in enumerate(numpy.linspace(-2,1,num=rows)):
    for coloumn_index,Im in enumerate(numpy.linspace(-2,1,num=rows)):
        result[row_index,coloumn_index]=mandelbrot(Re,Im,1000)
plt.figure(dpi=100)
plt.imshow(result.T,cmap='hot',interpolation='bilinear',extent=[-2,1,-1,1])
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()

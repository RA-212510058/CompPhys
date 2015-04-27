###QUESTION 1
import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

def Shift(y,n=0):
    y1=numpy.zeros(len(y))
    y1[n]=1     #position at where the gaussian is shifted
    y1_f=fft(y1)
    y_f=fft(y)
    return numpy.real(ifft(y1_f*y_f))

x=numpy.arange(-10,10,0.05)
y=numpy.exp(-0.5*(x/1.5)**2)
ys=Shift(y,len(y)/2)
plt.plot(x,y,label='Normal')
plt.plot(x,ys,label='Shifted')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='upper right')
plt.title('Shifted Gaussian using Convolution')
plt.show()

###QUESTION 2

import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

def Correlate(f,g):
    f1=fft(f)
    g1=numpy.conj(fft(g))
    return numpy.real(ifft(f1*g1))

x=numpy.arange(-10,10,0.05)
y=numpy.exp(-0.5*(x/1.5)**2)
yc=Correlate(y,y)
plt.plot(x,yc)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Correlation of a Gaussian with itself')
plt.show()

###QUESTION 3

import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

def Correlate(f,g):
    f1=fft(f)
    g1=numpy.conj(fft(g))
    return numpy.real(ifft(f1*g1))

def Shift(y,n=0):
    y1=numpy.zeros(len(y))
    y1[n]=1
    y1_f=fft(y1)
    y_f=fft(y)
    return numpy.real(ifft(y1_f*y_f))

x=numpy.arange(-10,10,0.05)
y=numpy.exp(-0.5*(x/1.5)**2)
ys=Shift(y,len(y)/5)
yc1=Correlate(y,y)
yc2=Correlate(ys,ys)
plt.plot(x,yc1,'r',label='Correlated')
plt.plot(x,yc2,'b--',label='Shifted and Correlated')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='upper right')
plt.title('Shift and Correlation of a Gaussian with itself')
plt.show()

#The correlation function is independant of the shift in the array

###QUESTION 4

import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

def Conv(x,y):
    x1=numpy.zeros(len(x)*2)
    y1=numpy.zeros(len(y)*2)
    x1[0:len(x)]=x
    y1[0:len(y)]=y
    xf=fft(x1)
    yf=fft(y1)
    z=numpy.real(ifft(yf*xf))
    return z[0:len(x)]

x=numpy.arange(-10,10,0.05)
y=numpy.exp(-0.5*(x/1.5)**2)
y=y/numpy.sum(y)      #normalises the gaussian
yc=Conv(y,y)
plt.plot(x,y,'r',label='Gaussian')
plt.plot(x,yc,'b--',label='Convolution')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='upper right')
plt.title('Convolution without circulant problem')
plt.show()

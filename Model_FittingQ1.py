import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,ifft

t=np.arange(0,10,0.1)
x=np.random.randn(100)    #row vector
xn=x.size

n=5  #order
vec=np.arange(0,xn)/(0.0+xn)*2*np.pi
M=np.zeros((xn,2*n-1))
M[:,0]=1.0
for i in range(1,n):
    M[:,2*i-1]=np.cos(i*vec)
    M[:,2*i]=np.sin(i*vec)

m=np.matrix(M)
mT=m.transpose()
FT=np.fft.fft(x)
xT=np.matrix(x).transpose()     #column vector
fit=np.linalg.inv(mT*m)*(mT*xT)

plt.plot(t,x,'o')
plt.plot(t,m*fit,'*')
plt.plot(t,np.real(FT))
plt.show()

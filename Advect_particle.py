import numpy
from matplotlib import pyplot as plt

def density(p,dx):
    pmin=numpy.min(p)
    pmax=numpy.max(p)
    nbin=numpy.round(1+(pmax-pmin)/dx) #no. of bins
    index=numpy.round((p-pmin)/dx) 
    rho=numpy.zeros(nbin)   #density array
    for i in numpy.arange(0,index.size):    #counts density of particles in each bin
        rho[index[i]]+=1.0
    x=numpy.arange(0,nbin)*dx+pmin   #x axis for the bins showing position
    return rho,x

n=10000   #no. of particles
xmax=1.0  #maximum particle position
v0=1.0    #max velocity
p=numpy.arange(n)/(0.0+n)*xmax    #creates the particles normalised
v=v0*(xmax-p)/xmax      #creates the velocity 'gradient' normalised
dt=0.01

plt.ion()
plt.plot(p)
plt.show()
plt.clf()
for ii in range(0,50):
    p+=v*dt    #updates particle positions
    rho,x = density(p,0.01)
    plt.plot(x,rho)
    plt.draw()

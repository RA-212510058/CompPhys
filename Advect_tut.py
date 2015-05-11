import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

n=300
v=-1.0
dx=1.0
x=np.arange(n)*dx
rho=np.exp(-0.5*((x-150)/30)**2)
dt=1.0
big_rho=np.zeros(n+1)
big_rho[:-1]=rho
for step in range(0,100):
    big_rho[:-1]=rho
    big_rho[-1]=big_rho[0]
    drho=big_rho[1:]-big_rho[0:-1]
    big_rho[:-1]=big_rho[:-1]-v*dt/dx*drho
    rho=big_rho[:-1]
    rho[0]=rho[0]-v*dt/dx*(rho[0]-rho[-1])
    plt.clf()
    plt.ion()
    plt.plot(x,rho)
    plt.draw()

#The function moves to the left and when it hits the left wall it
#comes back into the plot from the right. The total mass remains
#constant with time

######QUESTION 2

#The timestep dt changes with dx for constant velocity. If the 
#grid resolution is increased, dx is reduced and thus dt also 
#has to reduce to maintain stability. The amount of work increases 
#inverse proportionally to the decrease in timestep. eg. if the resolution is 
#increased by a factor of 10, dx has to decrease by a factor of 
#ten, thus dt also has to decrease by a factor of at least 10 to 
#still satisfy dt/dx<v. The amount of work is increased by a factor of 10 

#####QUESTION 3

#It remains stable as 1-a(1-exp(-ik)), where a=v*dt/dx, becomes 1 no
#matter the value of a

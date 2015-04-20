#QUESTION 1

import numpy
n=13
x0=0
x1=numpy.pi/2
dx=1.0/(n+1)
x=x1*numpy.arange(x0/x1,1+dx/2,dx)   #dx/2 allows the last point to be included
print x

#QUESTION 2

import numpy
import matplotlib.pyplot as plt
n=[10,30,100,300,1000]
x0=0
x1=numpy.pi/2
I=numpy.zeros(5)
for i in range(5):
    dx=1.0/(n[i]+1)
    x=x1*numpy.arange(x0/x1,1+dx/2,dx)
    y=numpy.cos(x)
    I[i]=sum(y)*dx*x1
print n
print I
plt.plot(n,I)
plt.xlabel('Points')
plt.ylabel('Absolute error')
plt.title('Integral of cosx from 0 to pi')
plt.show()
plt.savefig('Question 2b: Graph')

[10, 30, 100, 300, 1000]
[ 1.06969994  1.02512145  1.00775606  1.00260703  1.00078441]

#QUESTION 3

For odd:
x[1:len(x):2]
For even:
x[2:len(x)-1:2]

#QUESTION 4

import numpy
n=[10,30,100,300,1000]
x0=0
x1=numpy.pi/2
I=numpy.zeros(5)
for i in range(5):
    dx=1.0/(n[i]+1)
    x=x1*numpy.arange(x0/x1,1+dx/2,dx)
    y=numpy.cos(x)
    s=y[0]+y[-1]
    for j in range(1,len(x)-1,1):
        if j%2==0: #even points
            s+=2*y[j]
        if j%2!=0:  #odd points
            s+=4*y[j]
    I[i]=s*dx*x1/3
print n
print I

[10, 30, 100, 300, 1000]
[ 0.9965979   0.99957202  0.99995969  0.99999546  0.99999959]

#For Simpsons rule and using 11 points the integral is equal to 1.00000339
#To get the same answer using the normal method, 231530 points are needed
#Although Simpsons rule is meant to be used with even number of points

#QUESTION 5

import numpy
import matplotlib.pyplot as plt
n=[10,30,100,300,1000]
x0=0
x1=numpy.pi/2
In=numpy.zeros(5)  #normal summing
Is=numpy.zeros(5)  #Simpsons rule
for i in range(len(n)):
    dx=1.0/(n[i]+1)
    x=x1*numpy.arange(x0/x1,1+dx/2,dx)
    y=numpy.cos(x)
    In[i]=abs(sum(y)*dx*x1-1)
    s=y[0]+y[-1]
    for j in range(1,len(x)-1,1):
        if j%2==0:
            s+=2*y[j]
        if j%2!=0:
            s+=4*y[j]
    Is[i]=abs(s*dx*x1/3-1)
print n
print In
print Is
plt.plot(n,In,label='Normal')
plt.plot(n,Is,label='Simpson')
plt.xlabel('Points')
plt.ylabel('Absolute error')
plt.yscale('log')
plt.xscale('log')
plt.legend(loc='upper right')
plt.title('Integral of cosx from 0 to pi')
plt.show()
plt.savefig('Question 2e: Graph.jpeg')

import numpy as np
import matplotlib.pyplot as plt

class Nbody:
    dic={'Gravity':1,'Num':5}
    G=6.67428e-11
    def __init__(self,m=0,x=0,y=0,vx=0,vy=0):
        self.m=m
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    def copy(self):
        return Nbody(self.m,self.x,self.y,self.vx,self.vy)
    def distance(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return np.sqrt(x**2+y**2)
    def Pot(self,other):
        R=abs(self.distance(other))+0.0001
        return -1*self.dic['Gravity']*self.m*other.m/R
    def Kin(self):
        V=self.vx**2+self.vy**2
        return 0.5*self.m*V
    def Force(self,other):
        R=abs(self.distance(other))**3+0.0001
        mu=self.dic['Gravity']*self.m*other.m
        f=mu/R*self.VD(other)
        return f
    def VD(self,other):
        x=other.x-self.x
        y=other.y-self.y
        return np.array([x,y])
    def Update(self,data,f,dt):
        self.vx=data.vx+dt*f[0]/data.m
        self.vy=data.vy+dt*f[1]/data.m
        self.x=data.x+dt*data.vx
        self.y=data.y+dt*data.vy
         
def Num(data):
    return len(data)
def Create():
    data=Nbody(100,np.random.randn(),np.random.randn())
    return data
def Plot(data):
    #plt.clf()
    for i in range(len(data)):
        plt.plot(data[i].x,data[i].y,'ko-')
    plt.draw()
    
data=[]
data2=[]
N=2
for k in range(N):
    data.append(Create())
    data2.append(data[k].copy())


P=0.0
K=0.0
f=np.array([0,0])
tmin=0.0
tmax=2.0
dt=0.01
tsteps=int((tmax-tmin)/dt)
s=5000
plt.ion()
for t in range(0,tsteps,1):
    Plot(data)
    for tt in range(0,s):
        P=0.0
        K=0.0
        for i in range(N):
            for j in range(N):
                if j!=i:
                    f+=data[i].Force(data[j])       #total force on i
                if j>i:
                    P+=data[i].Pot(data[j])         #system total Ep
            data2[i].Update(data[i],f,dt/s)         #updates data2
            f*=0
        for a in range(N):
            K+=data[a].Kin()                            #total kinetic
        for k in range(N):
            data[k]=data2[k].copy()                 #updates data
    print(t,'Pot: ',P,'Kin: ',K,'E: ',(P+K))        #I am having a problem with conservation of energy especially when the particles get close to each other


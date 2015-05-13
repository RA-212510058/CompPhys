#QUESTION 1#######################################

#The assert is there to fail if none of the if statements are
#executed. ie. if self.bc_type is not 'periodic' or 'smooth' then 
#the assert fails, preventing the code from running and possible
#problems arising in the program

#QUESTION 2######################################

#The gradient is being calculated using the differences between values
#that are two steps apart instead of the usual one step, ie. (j+1)-(j-1)
#instead of (j-1)-(j), as an array of size 2 values smaller is needed. 
#Thus a half is needed to find the "average" of the differences

#QUESTION 3########################################

def get_timestep(self,dt=0.1):
    v=self.v.max()
    if v>0:    #to prevent division by 0
        T=self.dx/v    #as v*dt/dx <= 1, thus dt <= dx/v
    else:
        T=self.dx
    return T*dt


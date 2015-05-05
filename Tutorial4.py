###QUESTION 1

import numpy as np

class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def copy(self):    #Method to copy object
        return Complex(self.r,self.i)
    def __add__(self,val):    #Method for addition
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r+val.r
            ans.i=ans.i+val.i
        else:
            ans.r=ans.r+val
        return ans
    def __repr__(self):    #Method for printing
        if(self.i<0):
            return repr(self.r)+'-'+repr(-1*self.i)+'i'
        else:
            return repr(self.r)+'+'+repr(self.i)+'i'
    def __sub__(self,val):    #Method for subtraction
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r=ans.r-val.r
            ans.i=ans.i-val.i
        else:
            ans.r=ans.r-val
        return ans
    def __mul__(self,val):    #Method for multiplication
        ans=self.copy()
        a=self.copy()
        if isinstance(val,Complex):
            ans.r=a.r*val.r-a.i*val.i
            ans.i=a.r*val.i+a.i*val.r
        else:
            ans.r=ans.r*val
        return ans
    def __div__(self,val):    #Method for division
        ans=self.copy()
        if isinstance(val,Complex):
            num=ans*val.conj()
            den=val*val.conj()
            ans.r=float(num.r)/den.r
            ans.i=float(num.i)/den.r
        else:
            ans.r=float(ans.r)/val
        return ans
    def conj(self):      #Method to find the conjugate of a complex number
        ans=self.copy()
        if isinstance(ans,Complex):
            ans.i=-1*ans.i
        return ans

a=Complex(6,-7)
b=Complex(-3,9)
c=a+b
d=a-b
e=a*b
g=a/b
print('a: ',a)
print('b: ',b)
print('a+b: ',c)
print('a-b: ',d)
print('a*b: ',e)
print('a/b: ',g)

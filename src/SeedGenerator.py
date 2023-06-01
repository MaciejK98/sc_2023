import numpy as np
import matplotlib.pyplot as plt

class generator:
    def __init__(self,seed):
        self.seed=seed
        self.a=16807
        self.q=127773
        self.r=2836
        self.m =(self.a * self.q)+ self.r
        print(self.m)
        
    def UniformGenerator(self):
        # m=self.a*self.q+self.r
        h=(np.uint(self.seed/self.q)) 
        # print("h: ",h)
        # l= np.uint(self.seed%self.q)
        # test = self.a * l - self.r * h
        xx=(self.a*(self.seed - (self.q*h))) - (self.r*h)
        if (xx<0):
            xx=xx+self.m
        result=(xx/self.m)
        self.seed=xx
        return xx,result
    
    
  
      
# i= int(2147483647 /(100))
# print(i)  
# j=0
# seedGenerator = generator(2137)
# for j in range(1,i*100):
#   xx,result= seedGenerator.UniformGenerator()
#   if ( j%i==0 ):
    
#     print (xx)
#     # zapisac do pliku seedy
    
    
    

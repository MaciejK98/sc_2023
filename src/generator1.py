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
# seeds=[]
# j=0
# rng = generator(2137)   
# randoms=[]
# for i in range(47483647):
#     j=j+1
    
#     results,random=rng.UniformGenerator()
#     randoms.append(random)
#     if j==100000:
#         seeds.append(results)
#         print("histogram")
#         print("last result: ", results)
#         plt.hist(randoms)
#         plt.show()
#         print("po histogramie")
#         j=0

# print("seedy: ",seeds)
# rng2 = generator(results)   
# randoms=[]
# for i in range(100000):
#     results,random=rng2.UniformGenerator()
#     randoms.append(random)
# print("histogram")
# plt.hist(randoms)
# plt.show()
# print("po histogramie")
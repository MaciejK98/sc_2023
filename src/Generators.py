import numpy as np
import matplotlib.pyplot as plt

class UniformGenerator:
    def __init__(self,seed):
        self.seed=seed
        self.a=16807
        self.q=127773
        self.r=2836
        self.m =(self.a * self.q)+ self.r
        print(self.m)
        
    def Generate(self):
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

class ExponentialGenerator:
    def __init__(self, seed, intensity):
        self.seed = seed
        self.a = 16807
        self.q = 127773
        self.r = 2836
        self.m = (self.a * self.q) + self.r
        self.intensity = intensity

    def Generate(self):
        h = np.uint(self.seed / self.q)
        l = np.uint(self.seed % self.q)
        xx = self.a * l - self.r * h
        if xx < 0:
            xx = xx + self.m
        self.seed = xx

        # Generowanie liczby o rozkładzie wykładniczym
        result = -np.log(xx / self.m) / self.intensity

        return xx, result  

class NormalGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.a = 16807
        self.q = 127773
        self.r = 2836
        self.m = (self.a * self.q) + self.r

    def UniformGenerator(self):
        h = np.uint(self.seed / self.q)
        l = np.uint(self.seed % self.q)
        xx = self.a * l - self.r * h
        if xx < 0:
            xx = xx + self.m
        self.seed = xx
        return xx / self.m

    def Generate(self):
        u1, u2 = self.UniformGenerator(), self.UniformGenerator()
        r = np.sqrt(-2 * np.log(u1))
        theta = 2 * np.pi * u2
        x = r * np.cos(theta)
        return x

# Tworzenie generatora
seed = 2137
generator = NormalGenerator(seed)

# Generowanie próbki wartości o rozkładzie normalnym
sample_size = 100000
sample = [generator.Generate() for _ in range(sample_size)]

# Tworzenie histogramu
import matplotlib.pyplot as plt

plt.hist(sample, bins=30, edgecolor='black')
plt.xlabel('Wartość')
plt.ylabel('Częstość')
plt.title('Histogram próbki wartości o rozkładzie normalnym (metoda odwrotności dystrybuanty)')
plt.show()

# i= int(2147483647 /(100))
# # print(i)  
# j=0
# seedGenerator = UniformGenerator(2137)
# for j in range(1,i*100):
#   xx,result= seedGenerator.UniformGenerator()
#   if ( j%i==0 ):
    
#     print (xx)
    
      
# wykladniczy = ExponentialGenerator(2137,0.1)
# sample_size = 1000
# sample = []
# for _ in range(sample_size):
#     _, result = wykladniczy.Generate()
#     sample.append(result)

# # Tworzenie histogramu
# plt.hist(sample, bins=30, edgecolor='black')
# plt.xlabel('Wartość')
# plt.ylabel('Częstość')
# plt.title('Histogram próbki liczb o rozkładzie wykładniczym')
# plt.show()

# # Tworzenie generatora
# seed = 123
# generator = NormalGenerator(seed)

# # Generowanie próbki wartości o rozkładzie normalnym
# sample_size = 1000
# sample = [generator.Generate() for _ in range(sample_size)]

# # Tworzenie histogramu
# import matplotlib.pyplot as plt

# plt.hist(sample, bins=30, edgecolor='black')
# plt.xlabel('Wartość')
# plt.ylabel('Częstość')
# plt.title('Histogram próbki wartości o rozkładzie normalnym (metoda odwrotności dystrybuanty)')
# plt.show()
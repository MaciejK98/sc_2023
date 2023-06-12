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
        h = np.floor(self.seed / self.q)
        xx=(self.a*(self.seed - (self.q*h))) - (self.r*h)
        if (xx<0):
            xx=xx+self.m
        result=(xx/self.m)
        self.seed=xx
        return xx,result
        

def seedGenerator():
    seeds=[]
    seedGenerator = generator(123456)
    for i in range(10):
        for j in range(4):
            if j == 0:
                seeds.append([])  # Tworzenie listy dla każdego zestawu
            xx ,res = seedGenerator.UniformGenerator()  # Wygenerowanie jednego ziarna
            seeds[i].append(xx)  # Dodanie ziarna do odpowiedniego zestawu

            # Aktualizacja ziarna
            for _ in range(10000000):
                seedGenerator.UniformGenerator()  # Przesunięcie generatora o 10 milionów zmiennych

    # Wyświetlenie wygenerowanych ziaren
    for i in range(10):
        print(f"Zestaw {i+1}: {seeds[i]}")
        
    filename = "../seeds.csv"

    import csv

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        for item in seeds:
            writer.writerow(item)
            
seedGenerator()
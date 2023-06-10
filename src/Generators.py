import numpy as np
import matplotlib.pyplot as plt


class RNG:
    def __init__(self, seeds, intensity):
        self.seedEXP = seeds[0]
        self.seedUNI = seeds[1]
        self.seedNOR = seeds[2]
        self.seedNORB = seeds[3]
        self.a = 16807
        self.q = 127773
        self.r = 2836
        self.m = (self.a * self.q) + self.r
        self.intensity = intensity

    def GenerateUniform(self):  # LCG
        h = np.uint(self.seedUNI / self.q)
        xx = (self.a * (self.seedUNI - (self.q * h))) - (self.r * h)
        if xx < 0:
            xx = xx + self.m
        result = xx / self.m
        self.seedUNI = xx

        result = result * 45 + 5

        return xx, result  # [5,50]

    def GenerateExponential(self):  # LCG
        h = np.uint(self.seedEXP / self.q)
        xx = (self.a * (self.seedEXP - (self.q * h))) - (self.r * h)
        if xx < 0:
            xx = xx + self.m
        self.seedEXP = xx

        # Generowanie liczby o rozkładzie wykładniczym
        result = -np.log(xx / self.m) / self.intensity

        return result

    def UniformGeneratorForNormal(self, seed):
        h = np.uint(seed / self.q)
        xx = (self.a * (seed - (self.q * h))) - (self.r * h)
        if xx < 0:
            xx = xx + self.m
        seed = xx
        return xx / self.m, seed

    # NormalGenerator tak, aby generował wartości z rozkładu o średniej 0 i odchyleniu standardowym 4, możesz zastosować transformację Boxa-Mullera do generatora jednostajnego.
    # zmienne losowe z1 , z2 są niezależne i o rozkładzie normalnym
    def GenerateNormal(self):
        u1, newSeed = self.UniformGeneratorForNormal(self.seedNOR)
        u2, self.seedNOR = self.UniformGeneratorForNormal(newSeed)
        r = np.sqrt(-2 * np.log(u1))
        theta = 2 * np.pi * u2
        z1 = r * np.cos(theta)
        z2 = r * np.sin(theta)
        x = 4 * z1  # Odchylenie standardowe = 4
        y = 4 * z2  # Odchylenie standardowe = 4
        return x, y


def seedGenerator():
    seeds=[]
    seedGenerator = RNG([1, 1, 1, 1], 1)
    for i in range(10):
        for j in range(4):
            if j == 0:
                seeds.append([])  # Tworzenie listy dla każdego zestawu
            xx ,res = seedGenerator.GenerateUniform()  # Wygenerowanie jednego ziarna
            seeds[i].append(xx)  # Dodanie ziarna do odpowiedniego zestawu

        # Aktualizacja ziarna początkowego dla kolejnego zestawu
        for _ in range(10000000):
            seedGenerator.GenerateUniform()  # Przesunięcie generatora o 10 milionów zmiennych

    # Wyświetlenie wygenerowanych ziaren
    for i in range(10):
        print(f"Zestaw {i+1}: {seeds[i]}")
        
    filename = "seeds.csv"

    import csv

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        for item in seeds:
            writer.writerow(item)



if __name__ == '__main__':
# Tworzenie generatora
    seed = 2137
    generator = RNG([seed, seed, seed, seed], 0.35)

# Generowanie próbki wartości o rozkładzie normalnym
    sample_size = 1000000
    sample = []
    for n in range(sample_size):
        t1,t2 = (generator.GenerateNormal() )
        sample.append(t1)

# Tworzenie histogramów
    import matplotlib.pyplot as plt

    plt.hist(sample, bins=40, edgecolor='black')
    plt.xlabel('Wartość')
    plt.ylabel('Częstość')
    plt.title('Histogram próbki wartości o rozkładzie normalnym (metoda Boxa-Mullera) [0,4]')
    plt.show()

    sample = [generator.GenerateExponential() for _ in range(sample_size)]

    plt.hist(sample, bins=40, edgecolor='black')
    plt.xlabel('Wartość')
    plt.ylabel('Częstość')
    title = f"Histogram próbki wartości o rozkładzie wykładniczym z Lambda= {generator.intensity}"
    plt.title(title)
    plt.show()

    sample = [generator.GenerateUniform() for _ in range(sample_size)]

    plt.hist(sample, bins=90, edgecolor='black')
    plt.xlabel('Wartość')
    plt.ylabel('Częstość')
    title = "Histogram próbki wartości o rozkładzie jedostajnym z zakresu 5,50"
    plt.title(title)
    plt.show()




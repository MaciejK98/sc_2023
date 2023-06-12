import numpy as np
import matplotlib.pyplot as plt


class RNG:
    A = 16807
    Q = 127773
    R = 2836
    M = (A * Q) + R
    def __init__(self, seeds, intensity):
        self.seedEXP = seeds[0]
        self.seedUNI = seeds[1]
        self.seedNOR = seeds[2]
        # self.seedNORB = seeds[3]
        
        self.intensity = intensity

    def GenerateUniform(self):  # LCG
        h = np.floor(self.seedUNI / self.Q)
        
        x = (self.A * (self.seedUNI - (self.Q * h))) - (self.R * h)
        if x < 0:
            x = x + self.M
        result = x / self.M
        self.seedUNI = x

        result = result * 45 + 5

        return result  # [5,50]

    def GenerateExponential(self):  # LCG
        h = np.floor(self.seedEXP / self.Q)
        xx = (self.A * (self.seedEXP - (self.Q * h))) - (self.R * h)
        if xx < 0:
            xx = xx + self.M
        self.seedEXP = xx

        # Generowanie liczby o rozkładzie wykładniczym
        result = -1 * (1/self.intensity) * np.log(xx / self.M)  

        return result

    def UniformGeneratorForNormal(self, seed):
        h = np.floor(seed / self.Q)
        xx = (self.A * (seed - (self.Q * h))) - (self.R * h)
        if xx < 0:
            xx = xx + self.M
        seed = xx
        return xx / self.M, seed

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
    plt.ylabel('Częstość wystapień')
    plt.title('Histogram wartości z generatora o rozkładzie normalnym [0,4]')
    plt.show()

    sample = [generator.GenerateExponential() for _ in range(sample_size)]

    plt.hist(sample, bins=40, edgecolor='black')
    plt.xlabel('Wartość')
    plt.ylabel('Częstość wystapień')
    title = f"Histogram wartości z generatora o rozkładzie wykładniczym z Lambda= {generator.intensity}"
    plt.title(title)
    plt.show()

    sample = [generator.GenerateUniform() for _ in range(sample_size)]

    plt.hist(sample, bins=90, edgecolor='black')
    plt.xlabel('Wartość')
    plt.ylabel('Częstość wystapień')
    title = "Histogram wartości z generatora o rozkładzie jednostajnym z zakresu 5,50"
    plt.title(title)
    plt.show()


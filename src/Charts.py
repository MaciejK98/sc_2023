import csv
import matplotlib.pyplot as plt
import pandas as pd

# Wczytaj dane z pliku CSV

for seed in range(0, 10):
        # Wczytanie pliku CSV
        filename = f"../data/lambda/data_L=0.36_A=3.5_B=0_S={seed}.csv"
        df = pd.read_csv(filename)

filename = "../data/lambda/data_L=0.36_A=3.5_B=125_S=0.csv"
users_in_system = []
user_queue = []
count_current_location = 0

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Pomiń nagłówki

    for row in reader:
        users_in_system.append(int(row[4]))
        user_queue.append(int(row[5]))
        if float(row[2]) < 3000:  # Sprawdź warunek dla CurrentLocation
            count_current_location += 1

# Wygeneruj wykres
x = range(1, len(users_in_system) + 1)

plt.plot(x, users_in_system, label='UsersInSystem')
plt.plot(x, user_queue, label='UserQueue')

plt.xlabel('Liczba obsłużonych użytkowników')
plt.ylabel('Wartość')
plt.title('Wykres')
plt.legend()

plt.show()

# Wyświetl wartość, gdzie CurrentLocation < 3000
print("Liczba użytkowników rozłączona z warunku Delta:", count_current_location)

import csv
import matplotlib.pyplot as plt

# Wczytaj dane z pliku CSV
# filename = "data.csv"
handover_counter = []

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Pomiń nagłówki

    for row in reader:
        handover_counter.append(int(row[3]))

# Wygeneruj wykres histogramu
plt.hist(handover_counter, bins=range(min(handover_counter), max(handover_counter)+2), align='left')

plt.xlabel('Liczba przełączeń')
plt.ylabel('Liczba użytkowników')
plt.title('Rozkład liczby przełączeń użytkowników')

plt.show()

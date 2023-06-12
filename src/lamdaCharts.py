import pandas as pd
import matplotlib.pyplot as plt

# Inicjalizacja słownika, który będzie przechowywał dane dla poszczególnych lambd
lambda_data = {}

# Przechodzenie przez kombinacje parametrów
for lambda_val in range(32, 41, 2):
    # Inicjalizacja słownika dla danej lambdy
    lambda_dict = {'disconnected_users': [], 'avg_users': []}
    
    for seed in range(0, 10):
        # Wczytanie pliku CSV
        filename = f"../data/lambda/data_L={lambda_val/100}_A=3.5_B=0_S={seed}.csv"
        df = pd.read_csv(filename)
        
        # Dodawanie wartości do słownika dla danej lambdy
        lambda_dict['disconnected_users'].extend(df['DisconnectedUsers'])
        lambda_dict['avg_users'].extend(df['UsersInSystem'] + df['UserQueue'])
    
    # Obliczanie średnich wartości dla danej lambdy
    avg_disconnected_users = pd.Series(lambda_dict['disconnected_users']).unique()
    avg_avg_users = []
    
    for disconnected_users in avg_disconnected_users:
        avg_avg_users.append(
            pd.Series(lambda_dict['avg_users'])[pd.Series(lambda_dict['disconnected_users']) == disconnected_users].mean()
        )
    
    # Zapisywanie danych dla danej lambdy w słowniku
    lambda_data[lambda_val/100] = {'disconnected_users': avg_disconnected_users, 'avg_users': avg_avg_users}

# Tworzenie wykresu
plt.figure(figsize=(10, 6))

for lambda_val, data in lambda_data.items():
    disconnected_users = data['disconnected_users']
    avg_users = data['avg_users']
    
    plt.plot(disconnected_users, avg_users, label=f'Lambda = {lambda_val}')

plt.xlabel('Disconnected Users')
plt.ylabel('Average Number of Users')
plt.legend()
plt.title('Average Number of Users in System and Queue')
plt.grid(True)

# Wyświetlanie wykresu
plt.show()



# Inicjalizacja słownika, który będzie przechowywał dane dla poszczególnych lambd
lambda_data = {}

# Przechodzenie przez kombinacje parametrów
for lambda_val in range(32, 41, 2):
    # Inicjalizacja słownika dla danej lambdy
    lambda_dict = {'disconnected_users': [], 'avg_users': []}
    
    for seed in range(0, 10):
        # Wczytanie pliku CSV
        filename = f"../data/lambda/data_L={lambda_val/100}_A=3.5_B=125_S={seed}.csv"
        df = pd.read_csv(filename)
        
        # Dodawanie wartości do słownika dla danej lambdy
        lambda_dict['disconnected_users'].extend(df['DisconnectedUsers'])
        lambda_dict['avg_users'].extend(df['UsersInSystem'] + df['UserQueue'])
    
    # Obliczanie średnich wartości dla danej lambdy
    avg_disconnected_users = pd.Series(lambda_dict['disconnected_users']).unique()
    avg_avg_users = []
    
    for disconnected_users in avg_disconnected_users:
        avg_avg_users.append(
            pd.Series(lambda_dict['avg_users'])[pd.Series(lambda_dict['disconnected_users']) == disconnected_users].mean()
        )
    
    # Zapisywanie danych dla danej lambdy w słowniku
    lambda_data[lambda_val/100] = {'disconnected_users': avg_disconnected_users, 'avg_users': avg_avg_users}

# Tworzenie wykresu
plt.figure(figsize=(10, 6))

for lambda_val, data in lambda_data.items():
    disconnected_users = data['disconnected_users']
    avg_users = data['avg_users']
    
    plt.plot(disconnected_users, avg_users, label=f'Lambda = {lambda_val}')

plt.xlabel('Disconnected Users')
plt.ylabel('Average Number of Users')
plt.legend()
plt.title('Average Number of Users in System and Queue')
plt.grid(True)

# Wyświetlanie wykresu
plt.show()



# przedziały nieufnośći
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

# Inicjalizacja słowników
lambda_dict = {}
avg_users_dict = {}
confidence_intervals_dict = {}

# Przechodzenie przez kombinacje parametrów
for lambda_val in range(32, 41, 2):
    # Inicjalizacja list dla danej lambdy
    lambda_list = []
    avg_users_list = []
    
    for seed in range(0, 10):
        # Wczytanie pliku CSV
        filename = f"../data/lambda/data_L={lambda_val/100}_A=3.5_B=125_S={seed}.csv"
        df = pd.read_csv(filename)
        
        # Dodawanie wartości do list dla danej lambdy
        lambda_list.extend([lambda_val/100] * len(df))
        avg_users_list.extend(df['UsersInSystem'] + df['UserQueue'])
    
    # Zapisywanie list dla danej lambdy w słownikach
    lambda_dict[lambda_val/100] = lambda_list
    avg_users_dict[lambda_val/100] = avg_users_list

# Tworzenie wykresu
plt.figure(figsize=(10, 6))

for lambda_val, avg_users in avg_users_dict.items():
    lambdas = lambda_dict[lambda_val]
    
    # Obliczanie uśrednionych wartości avg_users dla danej lambdy
    avg_avg_users = []
    unique_lambdas = pd.Series(lambdas).unique()
    for unique_lambda in unique_lambdas:
        avg_users_values = pd.Series(avg_users)[pd.Series(lambdas) == unique_lambda]
        avg_avg_users.append(avg_users_values.mean())
        
        # Obliczanie przedziału nieufności
        std_error = avg_users_values.std() / np.sqrt(10)
        t_value = t.ppf(0.95, df=10-1)
        confidence_interval = t_value * std_error
        confidence_intervals_dict[unique_lambda] = [confidence_interval, confidence_interval]
    
    # Rysowanie punktów średnich
    x = [lambda_val]*len(unique_lambdas)
    y = avg_avg_users
    plt.plot(x, y, marker='o', markersize=5, label=f'Lambda = {lambda_val}')
    
    # Rysowanie przedziałów nieufności
    for i, unique_lambda in enumerate(unique_lambdas):
        yerr = confidence_intervals_dict[unique_lambda]
        plt.errorbar(x[i], y[i], yerr=np.array([yerr]).T, fmt='none', capsize=5, color='black')
    
    # Rysowanie poziomej kreski na poziomie 20
    plt.axhline(y=20, color='red', linestyle='--')

plt.xlabel('Lambda')
plt.ylabel('Average Number of Users')
plt.legend()
plt.title('Average Number of Users in System and Queue with Confidence Intervals')
plt.grid(True)

# Wyświetlanie wykresu
plt.show()


import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

lambda_values = range(32, 41, 2)
avg_avg_users = []
confidence_intervals = []

std_devs = []

for lambda_val in lambda_values:
    avg_users_lambda = []
    
    for seed in range(0, 10):
        # Wczytanie pliku CSV
        filename = f"../data/lambda/data_L={lambda_val/100}_A=3.5_B=125_S={seed}.csv"
        df = pd.read_csv(filename)
        
        sum_users = df['UsersInSystem'].sum() + df['UserQueue'].sum()
        avg_users = sum_users / len(df)
        avg_users_lambda.append(avg_users)
    
    avg_avg = np.mean(avg_users_lambda)
    std_dev = np.std(avg_users_lambda)
    std_devs.append(std_dev)
    avg_avg_users.append(avg_avg)
    
    # Obliczanie przedziału nieufności z rozkładu t-studenta
    dof = len(avg_users_lambda) - 1  # Stopnie swobody
    alpha = 0.05  # Poziom istotności (95% przedział ufności)
    t_value = t.ppf(1 - alpha/2, df=dof)  # Wartość krytyczna t dla danego poziomu istotności i stopni swobody
    margin_of_error = t_value * std_dev / np.sqrt(len(avg_users_lambda))  # Margines błędu
    
    confidence_interval = (avg_avg - margin_of_error, avg_avg + margin_of_error)
    confidence_intervals.append(confidence_interval)
    
    print(f"Lambda = {lambda_val}, Average = {avg_avg}, Standard Deviation = {std_dev}")
    print(f"Confidence Interval = {confidence_interval}")

# Tworzenie wykresu
x = list(lambda_values)
y = avg_avg_users
y_err = [ci[1] - ci[0] for ci in confidence_intervals]

plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5)
plt.xlabel('Lambda')
plt.ylabel('Average Users')
plt.title('Average Users with Confidence Intervals')
plt.xticks(x)
plt.grid(True)
plt.show()

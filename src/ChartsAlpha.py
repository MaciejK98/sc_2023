




import pandas as pd
import scipy.stats as stats

file_pattern = "../data/alpha/data_L=0.4_A=2.0_B=125_S={}.csv"

with open("wynikiA=2.txt", "w") as file:
    for s_value in range(10):
        filename = file_pattern.format(s_value)
        df = pd.read_csv(filename)
        
        handover_counter_values = df['Handovercouter'].values
        first_handover_location_values = df['FirstHandoverLocation'].values
        current_location_values = df['CurrentLocation'].values
        
        handover_counter_mean = handover_counter_values.mean()
        handover_counter_std = handover_counter_values.std()
        handover_counter_count = len(handover_counter_values)
        handover_counter_se = handover_counter_std / (handover_counter_count ** 0.5)
        handover_counter_ci = stats.t.interval(0.95, df=handover_counter_count-1, loc=handover_counter_mean, scale=handover_counter_se)

        first_handover_location_mean = first_handover_location_values[first_handover_location_values > 0].mean()
        first_handover_location_std = first_handover_location_values[first_handover_location_values > 0].std()
        first_handover_location_count = len(first_handover_location_values)
        first_handover_location_se = first_handover_location_std / (first_handover_location_count ** 0.5)
        first_handover_location_ci = stats.t.interval(0.95, df=first_handover_location_count-1, loc=first_handover_location_mean, scale=first_handover_location_se)
        
        user_count = len(df)
        current_location_count = df[df['CurrentLocation'] < 3000].shape[0]
        average_delta_disconnect = current_location_count / user_count
        delta_disconnect_std = (average_delta_disconnect * (1 - average_delta_disconnect) / user_count) ** 0.5
        delta_disconnect_se = delta_disconnect_std / (user_count ** 0.5)
        delta_disconnect_ci = stats.t.interval(0.95, df=user_count-1, loc=average_delta_disconnect, scale=delta_disconnect_se)

        print("Dla pliku", filename, file=file)
        print("srednia liczba handoverow:", handover_counter_mean, file=file)
        print("Przedzial ufnosci dla sredniej liczby handoverow:", handover_counter_ci, file=file)
        print("srednia liczba rozlaczonych uzytkownikow z warunku delta:", average_delta_disconnect, file=file)
        print("Przedzial ufnosci dla sredniej liczby rozlaczonych uzytkownikow z warunku delta:", delta_disconnect_ci, file=file)
        print("srednia wartosc FirstHandoverLocation:", first_handover_location_mean, file=file)
        print("Przedzial ufnosci dla sredniej wartosci FirstHandoverLocation:", first_handover_location_ci, file=file)
        print("------------------------------------", file=file)

# import pandas as pd

# file_pattern = "../data/alpha/data_L=0.4_A=2.0_B=125_S={}.csv"

# for s_value in range(10):
#     filename = file_pattern.format(s_value)
#     df = pd.read_csv(filename)
    
#     handover_counter_sum = df['Handovercouter'].sum()
#     current_location_count = df[df['CurrentLocation'] < 3000].shape[0]
#     current_location_sum = df['CurrentLocation'].sum()
#     first_handover_location_sum = df['FirstHandoverLocation'].sum()
#     user_count = len(df)

#     handover_average = handover_counter_sum / user_count
#     current_location_average = current_location_sum / user_count
#     first_handover_location_average = first_handover_location_sum / user_count
#     average_delta_disconnect = current_location_count / user_count 

#     print("Dla pliku", filename)
#     print("srednia liczba handoverow:", handover_average)
#     print("srednia liczba rozlaczonych uzytkownikow z warunku delta:", average_delta_disconnect)
#     print("srednia wartosc FirstHandoverLocation:", first_handover_location_average)
#     print("------------------------------------")

    import pandas as pd
    import scipy.stats as stats

    
    handover_counter_sum = 0
    current_location_count = 0
    current_location_sum = 0
    first_handover_location_sum = 0
    user_count = 0

    handover_counter_values = []
    first_handover_location_values = []

    for s_value in range(10):
        filename = file_pattern.format(s_value)
        df = pd.read_csv(filename)
        
        handover_counter_sum += df['Handovercouter'].sum()
        current_location_count += df[df['CurrentLocation'] < 3000].shape[0]
        current_location_sum += df['CurrentLocation'].sum()
        first_handover_location_sum += df['FirstHandoverLocation'].sum()
        user_count += len(df)
        
        handover_counter_values.extend(df['Handovercouter'].values)
        first_handover_location_values.extend(df[df['FirstHandoverLocation'] > 0]['FirstHandoverLocation'].values)

    handover_average = handover_counter_sum / user_count
    current_location_average = current_location_sum / user_count
    first_handover_location_average = first_handover_location_sum / user_count
    average_delta_disconnect = current_location_count / user_count

    handover_counter_std = pd.Series(handover_counter_values).std()
    handover_counter_se = handover_counter_std / (len(handover_counter_values) ** 0.5)
    handover_counter_ci = stats.t.interval(0.95, df=len(handover_counter_values)-1, loc=handover_average, scale=handover_counter_se)

    first_handover_location_std = pd.Series(first_handover_location_values).std()
    first_handover_location_se = first_handover_location_std / (len(first_handover_location_values) ** 0.5)
    first_handover_location_ci = stats.t.interval(0.95, df=len(first_handover_location_values)-1, loc=first_handover_location_average, scale=first_handover_location_se)

    delta_disconnect_std = (average_delta_disconnect * (1 - average_delta_disconnect) / user_count) ** 0.5
    delta_disconnect_se = delta_disconnect_std / (user_count ** 0.5)
    delta_disconnect_ci = stats.t.interval(0.95, df=user_count-1, loc=average_delta_disconnect, scale=delta_disconnect_se)

    print("Średnia liczba handoverów:", handover_average, file=file)
    print("Przedział ufności dla średniej liczby handoverów:", handover_counter_ci, file=file)
    print("Średnia liczba rozłączonych użytkowników z warunku delta:", average_delta_disconnect, file=file)
    print("Przedział ufności dla średniej liczby rozłączonych użytkowników z warunku delta:", delta_disconnect_ci, file=file)
    print("Średnia wartość FirstHandoverLocation:", first_handover_location_average, file=file)
    print("Przedział ufności dla średniej wartości FirstHandoverLocation:", first_handover_location_ci, file=file)
    print("------------------------------------")

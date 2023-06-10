import heapq
from .User import User
from .Generators import RNG
import csv
import os

filename = "seeds.csv"  # Nazwa pliku CSV
Seeds = []  # Lista do przechowywania zestawów ziaren
with open(filename, mode='r') as file:
    reader = csv.reader(file)

    for row in reader:
        seed_set = [int(seed) for seed in row]  # Konwersja ziaren na liczby całkowite
        Seeds.append(seed_set)  # Dodanie zestawu ziaren do listy
        

X= 2000
# alpha = 3.5
# LAMBDA = 0.4 #wieksza lambda - czesciej tworzących użytkowników max 0.4
# uuid=[]


class Simulator:
    test=True
    
    def __init__(self, Network, Lambda, Alpha, Begining, SeedSet):
        self.network = Network
        self.Generators= RNG(Seeds[SeedSet], Lambda)
        self.clock = 0
        self.alpha=Alpha
        self.agenda = []
        self.Begining = Begining
        self.directory= "data"
        self.datafilename =os.path.join(self.directory, f"data_L={Lambda}_A={Alpha}_B={Begining}_S={SeedSet}.csv")

    def run(self, howmuch):
        
        with open(self.datafilename, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Zapis nagłówków
            writer.writerow(['UserID', 'ConnectedBaseStation', 'CurrentLocation', 'Handovercouter', 'UsersInSystem', 'UserQueue', 'DisconnectedUsers'])
        
            print("Started Simulation, method: process interaction (M4):")
            id = 0
            user = User(id, X, self.alpha, self.clock, self.network, self.agenda, self.Generators,writer, self.Begining)
            user.activate(0)

            while self.network.DisconnectedUsers <= howmuch:
                if not self.agenda:
                    break

                process = heapq.heappop(self.agenda)
                self.clock = process.get_time()

                process.execute()

                if process.IsTerminated():

                    del process
            print("Finished Simulation, method: process interaction (M4):")
        # unique_values = set(uuid)
        # count = len(unique_values)
        # print(count)
        # print(uuid) 
        # self.network.DisconnectedUsers =0

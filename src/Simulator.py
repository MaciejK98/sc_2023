import heapq
from .User import User
from .Generators import RNG
import csv

seeds = [2137, 2137, 2137, 4]
X= 2000
alpha = 3.5
LAMBDA = 0.4 #wieksza lambda - czesciej tworzących użytkowników max 0.4
# uuid=[]
filename = "data.csv"

class Simulator:
    test=True
    
    def __init__(self, network):
        self.network = network
        self.Generators= RNG(seeds, LAMBDA)
        self.clock = 0
        self.agenda = []

    def run(self, howmuch):
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Zapisz nagłówki
            writer.writerow(['UserID', 'ConnectedBaseStation', 'CurrentLocation', 'Handovercouter', 'UsersInSystem', 'UserQueue'])
        
            print("Started Simulation, method: process interaction (M4):")
            id = 0
            user = User(id, X, alpha, self.clock, self.network, self.agenda, self.Generators,writer)
            user.activate(0)

            while self.network.DisconnectedUsers < howmuch:
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

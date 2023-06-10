import heapq
from .User import User
from .Generators import RNG

seeds = [2137, 1337, 80085, 58008]
X= 2000
alpha = 3.0
LAMBDA = 0.35

class Simulator:
    test=True
    
    def __init__(self, network):
        self.network = network
        self.Generators= RNG(seeds, LAMBDA)
        self.clock = 0
        self.agenda = []

    def run(self, howmuch):
        print("Started Simulation, method: process interaction (M4):")
        id = 0
        user = User(id, X, alpha, self.clock, self.network, self.agenda, self.Generators)
        user.activate(0)

        while self.network.DisconnectedUsers < howmuch:
            if not self.agenda:
                break

            process = heapq.heappop(self.agenda)
            self.clock = process.get_time()
            # print(self.clock)

            # print("Simulation Time:", self.clock)

            # process.sentUserReport(resultsFile)
            process.execute()
            # if int(self.clock %500) == 0.0 :
            #     if (self.clock %500) <0.02:
            #         print("Simulation Time:", self.clock)
                # print("Simulation Time:", self.clock)
            if process.IsTerminated():
                # heapq.heapify(self.agenda)
                # self.agenda.remove(process)
                # heapq.heapify(self.agenda)

                del process

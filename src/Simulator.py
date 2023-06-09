import heapq
from .User import User
from .Generators import UniformGenerator, ExponentialGenerator, NormalGenerator

seed = [2137, 1337, 80085, 58008]
X= 2000
alpha = 3.0
TTT=100 
WAITTIME= 20
DELTA = 20
LAMBDA = 0.5

class Simulator:
    test=True
    
    def __init__(self, network):
        self.network = network
        self.speedGenerator = UniformGenerator(seed[0])
        self.spawnTimeGenerator = ExponentialGenerator(seed[1],LAMBDA)
        self.BSApowerGenerator = NormalGenerator(seed[2])
        self.BSBPowerGenerator = NormalGenerator(seed[3])
        self.clock = 0
        self.agenda = []

    def run(self, time):
        print("Started Simulation, method: process interaction (M4):")
        id = 0
        user = User(id, X, self.speedGenerator, alpha, DELTA, TTT, WAITTIME, self.clock+5, self.network, self.agenda, self.spawnTimeGenerator, self.BSApowerGenerator, self.BSBPowerGenerator)
        user.activate(0)

        while self.clock < time:
            if not self.agenda:
                break

            process = heapq.heappop(self.agenda)
            self.clock = process.get_time()

            # print("Simulation Time:", self.clock)

            # process.sentUserReport(resultsFile)
            process.execute()
            if self.clock >500:
                pass
                # print("Simulation Time:", self.clock)
            if process.IsTerminated():
                # heapq.heapify(self.agenda)
                # self.agenda.remove(process)
                # heapq.heapify(self.agenda)

                del process

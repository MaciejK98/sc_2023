import heapq
from enum import Enum

class Process:
    class State(Enum):
        GENERATE_USER= 1
        CONNECTED_TO_BSA = 2
        CONNECTED_TO_BSB = 3
        DELETE_USER = 4

    def __init__(self, time, network, agenda):
        self.state = Process.State.GENERATE_USER
        self.time = float(time)
        self.terminated = False
        self.network = network
        self.agenda = agenda

    def execute(self):
        raise NotImplementedError

    def activate(self, time, relative=True):
        if relative:
            self.time += time
        else:
            self.time = time

        heapq.heappush(self.agenda, self)
        self.active = False

    def IsTerminated(self):
        return self.terminated

    def get_time(self):
        return self.time
    
    def __lt__(self, other):
        return self.time < other.time
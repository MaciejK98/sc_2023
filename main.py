from src.Network import Network
from src.Simulator import Simulator


if __name__ == '__main__':
    
    network = Network()
    simulator = Simulator(network)
    simulator.run(1000)
    

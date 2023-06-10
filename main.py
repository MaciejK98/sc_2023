import argparse
from src.Network import Network
from src.Simulator import Simulator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulator parameters')
    parser.add_argument('--Lambda', type=float, help='Lambda parameter')
    parser.add_argument('--Alpha', type=float, help='Alpha parameter')
    parser.add_argument('--Begining', type=int, help='Begining parameter')
    parser.add_argument('--UsersToHandle', type=int, help='n UsersToHandle')
    
    args = parser.parse_args()
    
    network = Network()
    simulator = Simulator(network, args.Lambda, args.Alpha, args.Begining)
    simulator.run(args.UsersToHandle)
    
# python main.py --Lambda 0.35 --Alpha 3.5 --Begining 10 --UsersToHandle 1000

import argparse
from src.Network import Network
from src.Simulator import Simulator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulator parameters")

    parser.add_argument("--LambdaMin", type=float, help="LambdaMin parameter")
    parser.add_argument("--LambdaMax", type=float, help="LambdaMax parameter")
    parser.add_argument("--LambdaStep", type=float, help="Lambda parameter")

    parser.add_argument("--AlphaMin", type=float, help="AlphaMin parameter")
    parser.add_argument("--AlphaMax", type=float, help="AlphaMax parameter")
    parser.add_argument("--AlphaStep", type=float, help="Alpha parameter")

    parser.add_argument("--Begining", type=int, help="Begining parameter")

    parser.add_argument("--SeedSet", type=int, help="SeedSetMin parameter")
    parser.add_argument('--UsersToHandle', type=int, help='n UsersToHandle')
   
    args = parser.parse_args()

    
    
    for l in range(int(args.LambdaMin * 100), int(args.LambdaMax * 100) + 1, int(args.LambdaStep * 100)):
        if args.AlphaStep != 0:
            for a in range(int(args.AlphaMin * 10), int(args.AlphaMax * 10) + 1, int(args.AlphaStep * 10)):
                for s in range(0, args.SeedSet, 1):
                    network = Network()
                    simulator = Simulator(network, l / 100, a / 10, args.Begining, s)
                
                    simulator.run(args.UsersToHandle)
                    del simulator
                    del network
        else:
            for s in range(0, args.SeedSet, 1):
                    network = Network()
                    simulator = Simulator(network, l / 100, args.AlphaMin, args.Begining, s)
                
                    simulator.run(args.UsersToHandle)
                    del simulator
                    del network
            
                

#python main.py --LambdaMin 0.3 --LambdaMax 0.4 --LambdaStep 0.02 --AlphaMin 3.5 --AlphaMax 3.5 --AlphaStep 0 --Begining 0 --SeedSet 1 --UsersToHandle 500

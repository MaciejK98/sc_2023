import argparse
from src.Network import Network
from src.Simulator import Simulator

def run_simulation(network, simulator, users_to_handle):
    simulator.run(users_to_handle)
    del simulator
    del network

def generate_simulator(network, lambda_val, alpha_val, beginning, seed_set):
    return Simulator(network, lambda_val, alpha_val, beginning, seed_set)

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

    lambda_range = range(int(args.LambdaMin * 100), int(args.LambdaMax * 100) + 1, int(args.LambdaStep * 100)) if args.LambdaStep else [int(args.LambdaMin * 100)]
    alpha_range = range(int(args.AlphaMin * 10), int(args.AlphaMax * 10) + 1, int(args.AlphaStep * 10)) if args.AlphaStep else [int(args.AlphaMin * 10)]

    for l in lambda_range:
        for a in alpha_range:
            for s in range(args.SeedSet):
                network = Network()
                simulator = generate_simulator(network, l / 100, a / 10, args.Begining, s)
                run_simulation(network, simulator, args.UsersToHandle)
                

# python main.py --LambdaMin 0.3 --LambdaMax 0.4 --LambdaStep 0.02 --AlphaMin 3.5 --AlphaMax 3.5 --AlphaStep 0 --Begining 0 --SeedSet 1 --UsersToHandle 500
# python main.py --LambdaMin 0.3 --LambdaMax 0.4 --LambdaStep 0.02 --AlphaMin 3.5 --AlphaMax 3.5 --AlphaStep 0 --Begining 125 --SeedSet 10 --UsersToHandle 525  
# python main.py --LambdaMin 0.36 --LambdaMax 0.36 --LambdaStep 0 --AlphaMin 3.5 --AlphaMax 4 --AlphaStep 0.5 --Begining 125 --SeedSet 10 --UsersToHandle 525 
# python main.py --LambdaMin 0.4 --LambdaMax 0.4 --LambdaStep 0 --AlphaMin 2 --AlphaMax 8 --AlphaStep 1 --Begining 125 --SeedSet 10 --UsersToHandle 525 
# python main.py --LambdaMin 0.36 --AlphaMin 3.5 --Begining 125 --SeedSet 1 --UsersToHandle 525 

import time
from src.generator1 import generator
from src.Network import Network 
from src.User import User
# from src.User import User 
# from src.Process import Process 
# from .src import src
generator(1)

network = Network(1,1,1,1,1)
user1 = User(111,50,3)
i=0
while user1.Location<3001:
  # print ("Silmulation goes brrr")
  i+=1
  # print(user1.ReportPower())
  # user1.ChangePosition()
  # print("              location", user1.Location)
  user1.execute()
  # time.sleep(0.1)
  # print(user1.Location)
  # break

print(i)
# import src.Process
# import src.lab1
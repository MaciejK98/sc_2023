import numpy as np

class User:
    # ConnectedBaseStation= "A"
    # DistanceToBaseStation= 2000
    
    def __init__(self):
        self.ConnectedBaseStation= 'A'
        self.DistanceToBaseStation= 2000 #meters
        self.MovementSpeed= self.GeneratedSpeed
        self.TimePassed= 20 #ms
        
    def GeneratedSpeed(): 
        return np.random(5,50) #change to proper generator
        
    def ChangePosition(self):
        self.DistanceToBaseStation+=self.MovementSpeed*self.TimePassed/1000
        
    def PwrReceived(self):
        # print("Received Power From Base Station")
        CalculatedPower=4.56 - 22*np.log10(self.DistanceToBaseStation)# + random
        return CalculatedPower
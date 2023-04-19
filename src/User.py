import random
import Process
import numpy as np

class User(Process):
    # ConnectedBaseStation= "A"
    # DistanceToBaseStation= 2000
    
    def __init__(self, user_id):
        self.UserId = user_id  # unikalny identyfikator użytkownika
        self.ConnectedBaseStation= 'Station A'
        self.Location= 2000 #meters
        self.MOVEMENTSPEED= self.GenerateSpeed
        self.WaitTime= 20 #ms
        
    def GenerateSpeed(): 
        return np.random(5,50) #change to proper generator
        
    def ChangePosition(self):
        self.DistanceToBaseStation+=self.MOVEMENTSPEED*self.TimePassed/1000
        
    def PwrReceived(self):
        # print("Received Power From Base Station")
        s = random.gauss(0, 4)
        CalculatedPower= {}
        CalculatedPower['Station A'] =4.56 - 22*np.log10(self.Location)+ s# + random
        CalculatedPower['Station B'] =4.56 - 22*np.log10(5000-self.Location)+ s# + random

        return CalculatedPower
    
    def CommitHandOver(self):
        if self.ConnectedBaseStation== 'Station A':
            self.ConnectedBaseStation= 'Station B'
        else:
            self.ConnectedBaseStation= 'Station A'
    
    def ReportPower(self):
        report = ""
        for station_id, power in self.PwrReceived.items():
            report += f"Station {station_id}: {power} dBm\n"
        return report
        
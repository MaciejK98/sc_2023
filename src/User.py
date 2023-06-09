import random
import numpy as np

from .Process import Process


class User(Process):
# class User:
    BaseStationAPower = 0
    BaseStationBPower = 0
    # DELTA = 20  # db difference to disconnect the user
    # state = 1
    
    ttt = 0  # 100ms -> 5 time
    # WAITTIME = 20  # ms
    # Location = 2000.0  # meters
    # timer=0

    def __init__(self, user_id, X, speedGenerator, alpha, delta, ttt, waitime, time, network, agenda, spawnTimeGeneratorm,BSApowerGenerator,BSBPowerGenerator):
        super().__init__(time, network, agenda)
        self.UserID = user_id  # unikalny identyfikator użytkownika
        self.ConnectedBaseStation = "Station A"
        self.StartLocation= X #2000 meters
        self.CurrentLocation= self.StartLocation #2000 meters
        self.SpeedGenerator = speedGenerator 
        self.Speed = self.SpeedGenerator.Generate()
        self.TTT= ttt
        self.WaitTime = waitime #20 ms
        self.STARTINGTTT = ttt/waitime # 100ms -> 5 times
        
        self.Timer= time
        self.DELTA =delta
        self.BSApowerGenerator= BSApowerGenerator
        self.BSBPowerGenerator= BSBPowerGenerator
        self.SpawnGenerator = spawnTimeGeneratorm
        # self.WaitTime= 20 #ms
        # self.BaseStationAPower = 0
        # self.BaseStationBPower = 0
        self.alpha = alpha  # optimization of this parameter

    def GenerateSpeed(self):
        return np.random(5, 50)  # change to proper generator

    def ChangePosition(self):
        self.CurrentLocation += self.Speed * self.WaitTime / 1000

    def PwrBSA(self):
        # Received Power From Base Station
        # s = random.gauss(0, 4)
        self.BaseStationAPower = 4.56 - 22 * np.log10(self.CurrentLocation) + self.BSApowerGenerator.Generate()  # + random

        return self.BaseStationAPower

    def PwrBSB(self):
        # Received Power From Base Station
        # s = random.gauss(0, 4)
        self.BaseStationBPower = (
            4.56 - 22 * np.log10(5000 - self.CurrentLocation) + self.BSBPowerGenerator.Generate()
        ) 

        return self.BaseStationBPower

    def CommitHandOver(self):
        if self.ConnectedBaseStation == "Station A":
            self.ConnectedBaseStation = "Station B"
        else:
            self.ConnectedBaseStation = "Station A"

    def ReportPower(self):
        report = f"Station A: {self.PwrBSA()} dBm\n"
        report += f"Station B: {self.PwrBSB()} dBm\n"
        report += f"position:  {self.CurrentLocation} "
        report += f"BS: {self.ConnectedBaseStation}"

        return report

    def disconnect(self):
        print("disconnected")
        pass

    def execute(self):
        active = True
        self.ChangePosition()
        # print(self.ReportPower())
        while active:
            
            # print(self.state)
            self.Timer= self.time
            
            match self.state:
                
                case self.State.GENERATE_USER:  # Generate user
                    self.network.addUser(self)
                    
                    self.network.AllUsers += 1
                    new_id = self.network.AllUsers + 1
                    # c=self.network.howMuchUsersInSystem()
                    
                    if self.network.howMuchUsersInSystem() < 20:
                        new_user = User(new_id, self.StartLocation, self.SpeedGenerator, self.alpha, self.DELTA, self.TTT, self.WaitTime, self.Timer, self.network, self.agenda, self.SpawnGenerator, self.BSApowerGenerator,self.BSBPowerGenerator)
                        new_user.activate(self.SpawnGenerator.Generate()) 
                    else:
                        self.network.UserQueue += 1
                    self.state = self.State.CONNECTED_TO_BSA

                                    
                case self.State.CONNECTED_TO_BSA:  # connected to BS-A
                    if (
                        self.BaseStationAPower - self.BaseStationBPower > self.DELTA
                    ):  # drop user
                        self.state = self.State.DELETE_USER

                    if self.BaseStationBPower - self.BaseStationAPower > self.alpha:
                        self.ttt -= 1
                        # print ("różnica mocy:    ", self.BaseStationBPower-self.BaseStationAPower)

                        if self.ttt <= 0:
                            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            self.CommitHandOver()
                            self.ttt = self.STARTINGTTT
                            self.state = self.State.CONNECTED_TO_BSB
                            
                        active = False
                        self.activate(0.02)
                    else:
                        self.ttt = self.STARTINGTTT
                        active = False
                        self.activate(0.02)
                    

                case self.State.CONNECTED_TO_BSB:  # connected to BS-B
                    if (
                        self.BaseStationBPower - self.BaseStationAPower > self.DELTA
                    ):  # drop user
                        # print ("różnica mocy:    ", self.BaseStationBPower-self.BaseStationAPower)
                        self.state = self.State.DELETE_USER

                    if self.BaseStationAPower - self.BaseStationBPower > self.alpha:
                        self.ttt -= 1
                        # print ("różnica mocy:    ", self.BaseStationAPower-self.BaseStationBPower)

                        if self.ttt <= 0:
                            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            self.CommitHandOver()
                            self.ttt = self.STARTINGTTT
                            self.state = self.State.CONNECTED_TO_BSA
                        active = False
                        self.activate(0.02)
                    else:
                        self.ttt = self.STARTINGTTT
                        active = False
                        self.activate(0.02)
                        
                case self.State.DELETE_USER:  # delete user
                    self.network.removeUserFromSystem(self)
                    self.terminated = True
                    active = False
            

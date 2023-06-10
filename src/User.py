# import random
import numpy as np

from .Process import Process


class User(Process):  # class User:
    BaseStationAPower = 0
    BaseStationBPower = 0
    DELTA = 25  # db difference to disconnect the user

    STARTINGTTT = 5
    ttt = 0  # 100ms -> 5 time

    def __init__(self, user_id, X, alpha, time, network, agenda, generators, writer, Begining):
        super().__init__(time, network, agenda)

        self.UserID = user_id  # unikalny identyfikator użytkownika
        self.ConnectedBaseStation = "Station A"
        self.StartLocation = X  # 2000 meters
        self.CurrentLocation = self.StartLocation  # 2000 meters

        self.Generators = generators
        self.Speed = self.Generators.GenerateUniform()

        self.Timer = time

        self.alpha = alpha  # optimization of this parameter
        self.Handovercouter =0
        
        self.writer= writer
        self.skipBegining = Begining

    def ChangePosition(self):
        
        self.CurrentLocation += self.Speed * 20 / 1000

    def CalulatePower(self):
        # Received Power From Base Station
        s1, s2 = self.Generators.GenerateNormal()
        self.BaseStationBPower = 4.56 - 22 * np.log10(5000 - self.CurrentLocation) + s1
        self.BaseStationAPower = 4.56 - 22 * np.log10(self.CurrentLocation) + s2

        return self.BaseStationAPower, self.BaseStationBPower

    def CommitHandOver(self):
        if self.ConnectedBaseStation == "Station A":
            self.ConnectedBaseStation = "Station B"
        else:
            self.ConnectedBaseStation = "Station A"
        self.ttt = self.STARTINGTTT
        self.Handovercouter += 1


    # def ReportPower(self):
    #     APwr, BPwr = self.CalulatePower()
    #     report = f"Station A: {APwr} dBm\n"
    #     report += f"Station B: {BPwr} dBm\n"
    #     report += f"position:  {self.CurrentLocation} "
    #     report += f"BS: {self.ConnectedBaseStation}"

        # return report
    
    def report(self):
        report =[self.UserID, self.ConnectedBaseStation, self.CurrentLocation, self.Handovercouter, self.network.howMuchUsersInSystem() ,self.network.UserQueue, self.network.DisconnectedUsers]
        return report

    # def IsDeltaConditionTrue(self, BSA, BSB):
    #     if self.BaseStationAPower - self.BaseStationBPower > self.DELTA:
    #         return True
    #     else:
    #         return False

    def disconnect(self):
        print("disconnected")
        pass


    def checkDistance(self):
        self.ChangePosition()
        if self.CurrentLocation >= 3000:
            self.state = self.State.DELETE_USER
            return True

    def execute(self):
        self.active = True
        self.Timer = self.time
       
        while self.active:
            
            match self.state:
                case self.State.GENERATE_USER:  # Generate user
                    
                    self.network.addUser(self)
                    
                    self.network.AllUsers += 1
                    new_id = self.network.AllUsers #+ 1
                    
                    new_user = User(new_id, self.StartLocation, self.alpha, self.Timer, self.network, self.agenda, self.Generators, self.writer, self.skipBegining)
                    new_user.activate(self.Generators.GenerateExponential())

                    if len(self.agenda) >= 21:
                        
                        self.active = False
                        self.terminated = True
                        
                    self.state = self.State.CONNECTED_TO_BSA

                case self.State.CONNECTED_TO_BSA:  # connected to BS-A
                    
                    if self.checkDistance(): continue
                    
                    self.CalulatePower()
                    
                    if self.BaseStationAPower - self.BaseStationBPower > self.DELTA:
                        self.state = self.State.DELETE_USER
                        continue

                    elif self.BaseStationBPower - self.BaseStationAPower > self.alpha:
                        self.ttt -= 1

                        if self.ttt <= 0:
                            self.CommitHandOver()
                            self.state = self.State.CONNECTED_TO_BSB

                    else:
                        self.ttt = self.STARTINGTTT
                    self.activate(0.02)

                case self.State.CONNECTED_TO_BSB:  # connected to BS-B
                    
                    if self.checkDistance(): continue
                    
                    self.CalulatePower()
                    
                    if self.BaseStationBPower - self.BaseStationAPower > self.DELTA:
                        self.state = self.State.DELETE_USER
                        continue

                    elif self.BaseStationAPower - self.BaseStationBPower > self.alpha:
                        self.ttt -= 1

                        if self.ttt <= 0:
                            self.CommitHandOver()
                            self.state = self.State.CONNECTED_TO_BSA

                    else:
                        self.ttt = self.STARTINGTTT
                    self.activate(0.02)

                case self.State.DELETE_USER:  # delete user
                    # report =
                    # print(report)
                    if self.network.DisconnectedUsers > self.skipBegining:
                        self.writer.writerow(self.report())
                    self.network.removeUserFromSystem(self)
                    
                    if self.network.UserQueue > 0:
                        new_user = User(self.network.AllUsers-self.network.UserQueue, self.StartLocation, self.alpha, self.Timer, self.network, self.agenda, self.Generators,self.writer, self.skipBegining)
                        new_user.state = self.State.CONNECTED_TO_BSA
                        new_user.activate(0.02)
                        self.network.UserQueue -= 1
                        self.network.addUser(new_user)
                    
                    self.terminated = True
                    self.active = False

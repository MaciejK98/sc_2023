import random

import numpy as np

from .Process import Process


# class User(Process):
class User:
    BaseStationAPower = 0
    BaseStationBPower = 0
    delta = 20  # db difference to disconnect the user
    state = 1
    ttt = 0  # 100ms -> 5 time
    WaitTime = 20  # ms
    Location = 2000.0  # meters

    def __init__(self, user_id, speed, alpha):
        self.UserID = user_id  # unikalny identyfikator użytkownika
        self.ConnectedBaseStation = "Station A"
        # self.Location= 2000.0 #meters
        self.MOVEMENTSPEED = speed
        # self.WaitTime= 20 #ms
        # self.BaseStationAPower = 0
        # self.BaseStationBPower = 0
        self.alpha = alpha  # optimization of this parameter

    def GenerateSpeed(self):
        return np.random(5, 50)  # change to proper generator

    def ChangePosition(self):
        self.Location += self.MOVEMENTSPEED * self.WaitTime / 1000

    def PwrBSA(self):
        # Received Power From Base Station
        s = random.gauss(0, 4)
        self.BaseStationAPower = 4.56 - 22 * np.log10(self.Location) + s  # + random

        return self.BaseStationAPower

    def PwrBSB(self):
        # Received Power From Base Station
        s = random.gauss(0, 4)
        self.BaseStationBPower = (
            4.56 - 22 * np.log10(5000 - self.Location) + s
        )  # + random

        return self.BaseStationBPower

    def CommitHandOver(self):
        if self.ConnectedBaseStation == "Station A":
            self.ConnectedBaseStation = "Station B"
        else:
            self.ConnectedBaseStation = "Station A"

    def ReportPower(self):
        report = f"Station A: {self.PwrBSA()} dBm\n"
        report += f"Station B: {self.PwrBSB()} dBm\n"
        report += f"position:  {self.Location} "
        report += f"BS: {self.ConnectedBaseStation}"

        return report

    def disconnect(self):
        print("disconnected")
        pass

    def execute(self):
        active = True
        while active:
            self.ChangePosition()
            print(self.ReportPower())
            # print(self.state)

            match self.state:
                case 1:  # connected to BS-A
                    if (
                        self.BaseStationAPower - self.BaseStationBPower > self.delta
                    ):  # drop user
                        self.disconnect()

                    if self.BaseStationBPower - self.BaseStationAPower > self.alpha:
                        self.ttt += 1
                        # print ("różnica mocy:    ", self.BaseStationBPower-self.BaseStationAPower)

                        if self.ttt >= 5:
                            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            self.CommitHandOver()
                            self.ttt = 0
                            self.state = 2
                    else:
                        self.ttt = 0

                case 2:  # connected to BS-B
                    if (
                        self.BaseStationBPower - self.BaseStationAPower > self.delta
                    ):  # drop user
                        # print ("różnica mocy:    ", self.BaseStationBPower-self.BaseStationAPower)
                        self.disconnect()

                    if self.BaseStationAPower - self.BaseStationBPower > self.alpha:
                        self.ttt += 1
                        # print ("różnica mocy:    ", self.BaseStationAPower-self.BaseStationBPower)

                        if self.ttt >= 5:
                            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            self.CommitHandOver()
                            self.ttt = 0
                            self.state = 1
                    else:
                        self.ttt = 0
            break

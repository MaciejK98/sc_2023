# import random
import queue

from .User import User


class Network:
    maxUsers = 20

    def __init__(self, l, n, alpha, delta, tau):
        self.l = l
        self.n = n
        self.alpha = alpha
        self.delta = delta
        self.tau = tau
        self.users = []
        self.t = 0

        self.fifo_queue = queue.Queue()

    def AddUser(self, currentUser):
        if len(self.users) < self.maxUsers:
            self.users.append(currentUser)
        else:
            self.fifo_queue.put(currentUser)

    def findUser(self, UserID):
        for user in self.users:
            # print(user)
            if user.UserID == UserID:
                return user

    def howMuchUsers(self):
        return len(self.users)

    # def create_user(self):
    #     x = random.uniform(0, self.l)
    #     v = random.uniform(1, 30)  # assume speed between 1 and 30 m/s
    #     user = User(x, v)
    #     self.users.append(user)

    # def run(self, tmax):
    #     for i in range(self.n):
    #         self.create_user()

    # while self.t < tmax:
    #     for user in self.users:
    #         if user.report_time == self.t:
    #             user.report_power()
    #             if user.connected_bs is None:
    #                 user.connected_bs = BS1 if user.x < self.l/2 else BS2
    #                 user.time_to_trigger = 1
    #             else:
    #                 user.time_to_trigger = max(0, user.time_to_trigger - self.tau)
    #         elif user.report_time == -1:
    #             self.users.remove(user)
    #     self.t += self.tau

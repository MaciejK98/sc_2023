# import random
import queue
# import heapq
# from .User import User


class Network:
    maxUsers = 20

    def __init__(self):
        # self.l = l
        # self.n = n
        # self.alpha = alpha
        # self.delta = delta
        # self.tau = tau
        self.users = []
        self.AllUsers =0
        self.UserQueue = 0
        # self.t = 0
        # self.time = 0.0

        self.fifo_queue = queue.Queue()

    def addUser(self, currentUser):
        if len(self.users) < self.maxUsers:
            # print(self.fifo_queue.qsize())
            # heapq.heappush(self.users_heap, currentUser)
            self.users.append(currentUser)
            print ("Added user")
        else:
            self.fifo_queue.put(currentUser)

    def findUser(self, UserID):
        for user in self.users:
            # print(user)
            if user.UserID == UserID:
                return user

    def removeUserFromSystem(self, user):
        if user in self.users:
            self.users.remove(user)
            
    def getUserFromQueue(self):
        return self.fifo_queue.get()
        
    def howMuchUsersInSystem(self):
        return len(self.users)

    def howMuchUsersInQueue(self):
        return self.fifo_queue.qsize()
    

class Network:
    maxUsers = 20

    def __init__(self):

        self.users = []
        self.AllUsers =0
        self.UserQueue = 0
        self.DisconnectedUsers = 0


    def addUser(self, currentUser):
        if len(self.users) < self.maxUsers:
            
            # heapq.heappush(self.users_heap, currentUser)
            self.users.append(currentUser)
            # print ("Added user")
        else:
            self.UserQueue += 1

    def findUser(self, UserID):
        for user in self.users:
            # print(user)
            if user.UserID == UserID:
                return user

    def removeUserFromSystem(self, user):
        if user in self.users:
            self.users.remove(user)
            self.DisconnectedUsers += 1
                 
    def howMuchUsersInSystem(self):
        return len(self.users)

    

# Que.5

# Write a class Train which has methods to book a ticket get status (no of sets)
# and get fair imformation of train running under indian railways

# import random

from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo =trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in trainNo:{self.trainNo} from {fro} to {to}")
       

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time.")
        

    def getfairinfo(self,fro, to):
        print(f"Ticket fare in tain no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

        # print(f"Ticket fare in tain no:{trainNo} from{fro} to{to} is {random.randint(222,5555)}")

t = Train(12399)
t.book("Pune","Mumbai")
t.getStatus()
t.getfairinfo("Pune","Mumbai")

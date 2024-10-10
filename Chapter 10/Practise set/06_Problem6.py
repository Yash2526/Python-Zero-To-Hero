
# Que.6

# Can you change the self parameter inside a class to something else(say"Harry").
# Try changing self to 'slf' or 'Harry' and see the effects.

from random import randint

class Train:
    def __init__(self,trainNo):     # We can change the attribute self - slf also.
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

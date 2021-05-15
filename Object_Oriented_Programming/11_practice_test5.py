''' Write a class train which has methods to book a ticket, get status(no of seats) and get fare 
    information of trains running under Indian Railways '''

class Train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare

    def bookticket(self):
        while (self.seats>0):
            print(f"Train {self.name} have {self.seats} seats, each person fare is {self.fare}")
            print("Your seat no is:",self.seats)  
            self.seats = self.seats-1
        else:
            print("all seats are booked")

book=Train("Bullet Express",5,250)
book.bookticket()

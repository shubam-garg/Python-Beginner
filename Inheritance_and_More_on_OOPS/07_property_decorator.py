class top:
    section="D"
    fee=20500
    
    @property # this method also known as getter method
    def netFee(self):
        return self.fee-self.discount

    @netFee.setter
    def netFee(self, net):
        self.fee=net-self.discount

t=top()
t.discount=500
print(t.netFee) # runnig as a property not a function
t.netFee=1900 # if I set the value hardcore
print(t.fee)
print(t.discount)
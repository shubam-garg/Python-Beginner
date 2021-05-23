class boss:
    def __init__(self,num):
        self.num=num
    
    def __str__(self):
        return f"{self.num}"

    def __len__(self):
        return 1
    
n=boss("money")
print(n)
print(len(n))
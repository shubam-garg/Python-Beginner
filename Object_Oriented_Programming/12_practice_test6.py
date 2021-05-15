# try to change self parameter in method and see the effects

class effect:
    def __init__(sky, no):
        sky.num = no

blue = effect(23) 
print(blue.num)
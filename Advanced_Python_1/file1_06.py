def welcome(name):
    print(f"Hello, {name} Here is your CEO")

# print(__name__)
if __name__=="__main__": # to run this file in current program only. 
    n=input("Enter your name: ")
    welcome(n)
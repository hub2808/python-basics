accbal=1000000
print("enter 1 to withdraw or enter 2 to deposit")
a=int(input("enter the value"))
amt=int(input("enter amount"))
accbal1=0
accbal2=0
def withdraw(amt):
    accbal1=accbal+amt
    print("the current balance",accbal1)
def deposit(amt):
    accbal2=accbal-amt
    print("the current balance",accbal2)
if a ==1:
    withdraw(amt)
else:
    deposit(amt)
            

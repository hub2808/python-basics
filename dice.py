import random
def ran():
    print(random.randint(1,9))
i=1
while(i<=5):
    a=int(input("enter the value"))
    if(a==ran()):
        print ("success")
    else:
        print ("try again")
        i+=1;
        

import random

def check(computer,user):
    if computer==user:
        return 0
    if computer==0 and user==1:
        return -1
    if computer==1 and user==2:
        return -1
    if computer==2 and user==0:
        return -1
    else:
        return 1

computer=random.randint(0,2)
user=int(input("o for snake ,1 for water , 2 for gun:"))

score  =check(computer,user)
print("you:" ,user)
print("computer:",computer)

if(score==0):
    print("its a tie")
elif(score==-1):
    print("You lose")
else:
    print("you won")

          






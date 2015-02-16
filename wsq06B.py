#By: Luis Carlos Najera  Date:(12/02/2015) SN:A01630557
#Python 3.4.0(Linux Ubuntu 14.04 Terminal Default)
#WSQ06 #Mastery05
import random
for i in range(1):
    x=random.randint(0,100)
number=0
i=0
print("This Program Will Generate A Random Number Between 0 And 100 And The User Have To Guess It.")
while(number!=x):
    i=i+1
    number=int(input("Choose A Number Between 0 and A 100"))
    if(number>x):
        print("Sorry but your number is to high")
    else:
        if(number<x):
            print("Sorry but your number is to Low")
        else:
            print("You Got It Dude")
            print("It Takes You",i,"Times to guess the number")

#By: Luis Carlos Najera
#Python 3.4.0(Linux Ubuntu 14.04 Terminal Default)
#WSQ06

import random                   #Import The Library In Charge of Generate Random Numbers
for i in range(1):
    x=random.randint(0,1024)     #Set The Inferior and Superior limits For Our Random Int
num=101
i=0
print("This Program will generate a random number between 0 and 1024, you have to write any numbers you want until you hit the random number, good luck")
while(num!=x):
    i=i+1
    num=int(input("Choose A Number between 0 and 1024 "))
    if(num>x):
        print("Sorry But The Number You Choose is Too High")
    else:
        if(num<x):
            print("Sorry But The Number You Choose is Too Low")
        else:
            if(num==x):
                print("You Got It Dude")
                print("It Takes You ",i," Times To Guees")

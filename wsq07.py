#By: Luis Carlos Najera
#Python 3.4.0(Linux Ubuntu 14.04 Terminal Default)
#WSQ07
print("This Program will solve the summatory of numbers asking for a Lower and an Upper Limit, The Upper And Lower Limit are included in the Summatory")
LL=0
UL=0
r=0
LL=int(input("Type the lower limit of your Summatory "))
UL=int(input("Type the upper limit of your Summatory "))
if LL>=UL:
    print("Invalid Entry, The Lower Limit Should Be Minor than the Upper Limit")
while(LL<=UL):
    r=r+LL
    LL=LL+1
print("The Summatory Result is ",r)



#By: Luis Carlos Najera
#Python 3.4.0(Linux Ubuntu 14.04 Terminal Default)
#WSQ05
print("This Program Will Convert temperatures from Celsius to Fahrenheit and from Fahrenheit to Celsius")
inp=str(input("Type the First Letter of the unit you want to Get (C for Celsius & F for Fahrenheit) "))
data=int(input("Now Type the number to convert "))
if(inp=="F" or inp=="f"):

    result=.55555*(data-32)
    name="Celsius"

else:
    result=1.8*(data)+32
    name="Fahrenheit"

print("The Result Of The convertion is",result," ",name)

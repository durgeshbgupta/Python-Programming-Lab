a=int(input("enter the temp"))
b=int(input("if temp entered is in celcius enter 1 or else press 2"))
if b==1:
 c=(9*a +160)/5
 print("temp in farenheit is",c)
else:
 c=(5*a -160)/9
 print("temp in celcius is:",c)

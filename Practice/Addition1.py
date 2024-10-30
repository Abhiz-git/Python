No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter the No1: "))
No2 = int(input("Enter the No2: "))

Ans = No1 + No2

print("Answer is: ", Ans)

"""
the cahnge in this code from previous code is on line 5,6,10
changes are "typecasting" str into int on line 5 & 6.
In various python version "+" is used for concatenation thats why on line no 10 the change is use ',' instead of '+'
after statement and before Ans var., even if we just separate +Ans and satement (Addition.py) with , still our logic gives desired output

"""
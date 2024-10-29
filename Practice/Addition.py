No1 = 0
No2 = 0
Ans = 0

No1 = input("Enter first number : ")
No2 = input("Enter second number : ")

Ans = No1 + No2

print("Addition is : "+Ans)


'''
even after asigning 0 that is int to variables No1, No2, and Ans on line no 1,2,3 though the output is concatenation of variable value becoz there is no fixed typing in python
As variable No1 and No2 is converting into 'str' datatype (default datatype of input())
the output of ans is Concatenated bcoz of '+' sign on line no. 8
'''

def Addition(No1, No2):
    Result = 0
    Result = No1 + No2
    return Result


def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    Answer = 0
    Answer = Addition(Value1, Value2)

    print("Addition is : ",Answer)

main()

"""
As per the comments of file main.py
this code follows rule of Interpreter that is line no 17 is self excutable and at 0th level.
But its not good code of practice.
"""
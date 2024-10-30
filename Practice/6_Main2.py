
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

if __name__ == "__main__":
    main()


"""
on Line no 17 we have use spcial variable (_ _<any>_ _)
__name__ is used to see current module name
__main__ underline this variable is used to know main page of code
Here, on line 17,18 states the condition that if this page is '__main__' call main()

this type of coding is know as exclusively adding of Entry point for better understanding of code
"""

def CheckEvenOdd(No):

    Result = No % 2

    if Result == 0:
        print(No,"is Even No.")
    else:
        print(No, "is Odd No.")



def Main():

    No = 0                              #its code programming practice but not mandatory
    No = int(input("Eneter the No.: "))

    CheckEvenOdd(No)


if __name__ == "__main__":
    Main()
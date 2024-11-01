
def Main():

    print("Enter No.1: ")
    No = int(input())

    Result = No % 2

    if Result == 0:
        print(No,"is Even No.")
    else:
        print(No, "is Odd No.")


if __name__ == "__main__":
    Main()
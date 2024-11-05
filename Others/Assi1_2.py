def ChkNum(No):

    if No % 2 == 0:
        return True


def Main():

    no = 0
    no = int(input("Enter the Number to check: "))
    result = False
    result = ChkNum(no)

    if result == True:
        print(no,"Is Even")
    else:
        print(no,"Is Odd")


if __name__ == "__main__":
    Main()
def Add(a,b):
    return a + b


def Main():
    no1 = no2 = 0
    no1 = int(input("Enter 1st no.: "))
    no2 = int(input("Enter 2nd no.: "))

    print(f"Addition of Enter no {no1} & {no2} is:",Add(no1,no2))


if __name__ == "__main__":
    Main()
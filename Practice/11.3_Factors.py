
def DisplayFactors(value):

    for i in range(1,value):

        if value % i == 0:
            print(i)


def Main():

    no = 0

    no = int(input("Enter the no to find factors of: "))

    DisplayFactors(no)


if __name__ == "__main__":
    Main()    
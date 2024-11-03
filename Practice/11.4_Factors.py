
def DisplayFactor(value):
    no = 1
    while( no < value):

        if value % no == 0:
            print(no)
        
        no = no + 1


def Main():

    no = 0

    no = int(input("Enter the no to find factor of: "))

    DisplayFactor(no)


if __name__ == "__main__":
    Main()
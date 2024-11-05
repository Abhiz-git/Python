"""
Question: Count character in Name and print it
Example: Abhi D Nale -> 9
                        A
                        b
                        h
                        i

                        D

                        N
                        a
                        l
                        e
"""
def CntChar(name):
    cnt = 0
    for char in name:
        cnt = cnt + 1
        if char == " ":
            cnt = cnt - 1
        
    return cnt


def Char(Name):

    for char in Name:
        print(char)


def Main():

    name = ""
    name = input("Enter your Name: ")

    print(f"Number of characters in your name are {CntChar(name)}")
    print("Characters in your name are:")
    Char(name)


if __name__ == "__main__":
    Main()
"""
Question: Count character in Name
Example : name = Abhi Nale -> char in name are 8
"""

def CntChar(name):

    cnt = 0
    for char in name:
        cnt = cnt + 1
        if char == " ":
            cnt = cnt - 1
    
    return cnt
 

def Main():
    
    name = ""
    name = input("Enter your name: ")

    print("Characters in name are",CntChar(name))


if __name__ == "__main__":
    Main()
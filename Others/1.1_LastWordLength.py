
"""
Question: Find out length of a last word in a String.

"""
def LastWordCnt(String):

    s = String.split()

    word = ""
    for word in s:
        pass

    return len(word) 

def Main():

    String = input("Enter a string: ")

    print("Lenght of Last word in string is: ", LastWordCnt(String))


if __name__ == "__main__":
    Main()
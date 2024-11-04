
"""
Question: Find out length of a last word in a String.

"""



def LastWordLen(String):

    s = String.split()

    cnt = len(s[-1])

    return cnt


def Main():

    String = input("Enter the String here: ")

    print("Length of last word is", LastWordLen(String))


if __name__ == "__main__":
    Main()
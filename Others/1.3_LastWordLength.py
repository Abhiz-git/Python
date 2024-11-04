
def LastWordLen(String):

    
    space = 0
    for char in String:

        if char == " ":
            space = space + 1
    cnt = 0
    count = -1
    for word in String:

        if word == " ":
            cnt = cnt + 1
        
        if cnt == space:
            count = count + 1

    print(count)
    return count


def Strip(String):
    S = ""
    if String[0] == " ":
        S = String[1:]
        print(S[0])
    else:
        S = String

    cnt = 0
    A = ""
    for i in S:
        cnt = cnt + 1

    if S[cnt-1] == " ":
        A = S[:cnt-1]

    print(A, end = " ")


def Main():

    String = input("Enter a string here: ")

    S = ""
    #print(2,end="")
    S = Strip(String)

    print(1)
   #print("Last Word lenght in a string is: ", LastWordLen(S))

if __name__ == "__main__":
    Main()
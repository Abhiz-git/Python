
def LastWordLen(String):

    space = 0
    cnt = 0
    count = -1

    # counts the blank spaces in string 
    for char in String:
        if char == " ":
            space = space + 1
    # compare the blank space from previous loop with this loop
    for char in String:
        if char == " ":
            cnt = cnt + 1
    # once the cnt variable matches with total blank spaces then it counts the characters of further word
        if cnt == space:
            count = count + 1

    return count


def Main():

    String = input("Enter a string here: ")
    String = String.strip()
    print("lenght of last Word in string is: ", LastWordLen(String))


if __name__ == "__main__":
    Main()


"""
Difference:
        difference between previous codes(1,1.1) and this code is that I have not use any inbuild function to satisfy the questions output
        only inbuild function in this code is .strip() that to pass the test cases

Logic:
    as per the question Last word of the string means, word after the last whitespace will be the last word.
    so here,
        in 1st for-loop (line no.(l.no.): 9) for loop is counting the total no of whitespaces in given string and stores the count in variable space.
        in 2nd for-loop (l.no: 12) this loop initialy (1st if-condition) again counts the total whitespaces in given string and store it in variable cnt,
            2nd if-condition(l.no.: 17) check that variable cnt is equal to the variable space(total whitespace in string).
        therefore as per the l.no.: 40, character after the last whitespace is counted as it will be the last word of string and stored that count into variable count,
            which is than return to the caller.
"""
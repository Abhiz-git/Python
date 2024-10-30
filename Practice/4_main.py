
def Addition(No1, No2):
    Result = 0
    Result = No1 + No2
    return Result


def main():
    Value1 = int(input("Enter First Number"))
    Value2 = int(input("Enter Second Number"))

    Answer = 0
    Answer = Addition(Value1, Value2)

    print("Addition is : ",Answer)


"""
Python code excutes from 1st line which is defiened at its 0th level of indentation and its must be "self executable"
here in this code on line 2 and 8 both def keywords are at 0th level but they are callable keywords i.e they are not self executable.
thus cursor checks every line from line no.1 and finally at line 16 as there is no further instructions it stops and in this range doesnt find any statement or instruction that fits in the rule of Interpreter.
Therefore, execution stops and code is terminated without displaying any output.
"""
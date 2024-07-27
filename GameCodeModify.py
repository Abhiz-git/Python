from random import randint as r
from time import sleep as de
def Square():
    ques = r(1, 100)
    print(f"What is the Square of {ques}: ")
    ans = int(input())
    if (ques*ques) == ans:
        print(f"Right, {ans} is a sqare root of {ques}")
        return 1
    else:
        print("Oops..! Wrong answer")
        return 0
def Code(name):

    if name == "":
        name = input("please enter name")
    print("welcome ", name)

def SqRoot():
    ques = r(1, 100)
    ques *= ques
    print(f"What is the Square root of {ques}: ")
    ans = int(input())
    if ques == (ans * ans):
        print(f"{ans} is a square root of {ques}\n")
        return 1
    else:
        print("oops..! Wrong answer")
        return 0

def main():
    name = input("Please enter your name: ")

    while not name.isalpha():                                      # name is String check
        name = input("Please enter Valid name: ")

    c = 0
    while(c!=3):
            shuffle = r(0,1)
            if(shuffle == 1):
                    a = SqRoot()
                    if(a == 0):
                        c = 0
                    else:
                        c += 1

            else:
                a = Square()
                if a == 0:
                    c = 0
                else:
                    c += 1

            if c == 1:
                print("Congratulations", "!"*((2 ** 3)+1))
            elif c == 2:

                print("Congratulations", "!"*((2 ** 1)+1))
           # elif c == 3:
            #   print(f"\n Congratulations {name} \U0001F600 ")

            if c != 3:
                permission = int(input("Would you like to  continue? yes-> 1 no-> 0: "))
                if permission == 1:
                    print(" ")
                    pass
                else:
                        print(f"{name} is a losser ")
                        de(5)
                        end = input("Still you would like to exit yes/no: ")
                        if(end == 'yes' or 'Yes' or 'exit'):
                            exit(0)
                        elif(end == 'no' or 'No' or 'NO' or 'continue'):
                            exit(0)

    print(f"\n Congratulations ! {name} \U0001F600 ")
    de(5)


if __name__ == '__main__':
    main()



'''
1st -> !!!
2nd -> !!
3rd -> !
Congratulations {Name} smile
'''
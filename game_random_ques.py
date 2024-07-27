import random
from time import sleep as delay

def sameer():
    global count
    print(f"The data type of {name} is {type(name)}")
    question = random.randint(1, 100)
    question = question * question

    print(f"What is the square root of {question}? ")
    Answer = int(input())
    print(f"The data type of {Answer} is {type(Answer)}")

    if (question == Answer * Answer):
        count += 1
        print("Your answer is right")
    else:
        count = 0
        print("Your answer is wrong")

    if (count == 3):
        print(f"{name} won congratulation")
        delay(10)
        return

    else:
        print("Do you want to continue? Continue:1, Exit:0")
        ans = int(input())

        if (ans == 1):
            pass
        else:
            print(f"{name} is loser")
            return 0
def abhishek():
    global count
    print(f"The data type of {name} is {type(name)}")
    question = random.randint(1, 100)
    print(f"What is the square of {question}? ")
    Answer = int(input())
    print(f"The data type of {Answer} is {type(Answer)}")

    if (question * question == Answer):
        count += 1
        print("Your answer is right")
    else:
        count = 0
        print("Your answer is wrong")

    if (count == 3):
        print(f"{name} won congratulation")
        delay(10)
        return

    else:
        print("Do you want to continue? Continue:1, Exit:0")
        ans = int(input())

        if (ans == 1):
            pass
        else:
            print(f"{name} is loser")
            return 0


name = input("Enter your name:")
print("Hii", name, "Welcome to the game")

count = 0

while (count!=3):
   ran=random.randint(0,1)
   if(ran==1):
       sameer()
   else:
       abhishek()

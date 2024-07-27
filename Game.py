import random
from time import sleep as delay

name = input("Enter your name:")
print("Hii", name, "Welcome to the game")
chinmay = True; count=0
while(chinmay):
                        print(f"The data type of {name} is {type(name)}")
                        question = random.randint(1,100)
                        print(f"What is the square of {question}? ")
                        Answer = int(input())
                        print(f"The data type of {Answer} is {type(Answer)}")

                        if(question*question == Answer):
                            count+=1
                            print("Your answer is right")
                        else:
                            count=0
                            print("Your answer is wrong")

                        if(count==3):
                            print(f"{name} won congratulation")
                            delay(10)
                            break

                        else:
                            print("Do you want to continue? Continue:1, Exit:0")
                            ans = int(input())

                            if(ans==1):
                                pass
                            else:
                                print(f"{name} is loser")
                                break


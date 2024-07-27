import random

n=str(input("Enter your name"))
print("welcome ",n)
# i=int(input("Enter num"))
# print("to exit game Enter 0")
cnt=0

while(cnt!=3 ):
    r=random.randint(1,100)
    sq=r*r
    print("what is sq of",r)
    num=int(input("Enter answer or enter 0 to exit"))
    if(num==0):
        breakaa
    if(sq==num):
        print("Keep it up")
        cnt+=1
    else:
        print("try again")
    if(cnt==3):
        print("your are winner")

"""
question enter the name (first and Last) count characters in full name and print name that many times
Example: name: Abhi Nale-> Abhi 
                           Abhi 
                           Abhi 
                           Abhi 

                           Nale 
                           Nale 
                           Nale

"""
# Solution <Solved using without inbuild Functions >


def SplitX(String):
    
    l=[]; Str=""
    sWords= 0

    for char in String:

        if char != " ":
            Str = Str + char
        
        else:
            l.append(Str)
            Str=""
    l.append(Str)
    return l


def Words(String):
    
    lst=[]
    cntw = 0

    lst = SplitX(String)

    for words in lst:
        cntw = cntw + 1
    
    for i in range(cntw):

        for _ in lst[i]:
            print(lst[i])

        print()


def Main():
    
    String = input("Enter your first and last name: ")

    String = String.strip()
    Words(String)


if __name__ == "__main__":
    Main()
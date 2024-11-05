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


def Split(String):

    lst = list()
    Str = ""
    String = String+" "
    for char in String:
        if char != " ":
            Str = Str+char
        else:
            lst.append(Str)
            Str = ""

    return lst

def Words(String):
    
    i = cntL = cntw = 0
    lst1 = list()
    String = String.strip()
    lst1 = Split(String)

    for char in lst1:
        cntL = cntL + 1
    
    while(i < cntL):
        
        for char in lst1[i]:
            cntw = cntw + 1

        for times in range(cntw):
            print(lst1[i])
            
        cntw = 0
        i = i + 1 


def Main():
    
    String = input("Enter your first and last name: ")

    Words(String)


if __name__ == "__main__":
    Main()
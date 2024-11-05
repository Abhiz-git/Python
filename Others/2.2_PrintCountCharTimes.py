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
# Solution <Solved using inbuild Function>

def Words(String):
    
    S = String.split(" ")

    i=0
    while(i<len(S)):
        for _ in range(len(S[i])):
            print(S[i])

        i = i + 1

def Main():
    
    String = input("Enter your first and last name: ")

    String = String.strip()
    Words(String)


if __name__ == "__main__":
    Main()
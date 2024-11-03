
no = 0 
no = int(input("Enter the no of which factors to find: "))

for i in range(1,no,1):
    
    if no % i == 0:
        print(i)


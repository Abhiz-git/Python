
def Main():
    
    length = int(input("Enter the no of elements that you want to store: "))

    arr = list()

    print("Enter the elements you want to insert: ")
    for i in range(length):
        value = int(input())
        arr.append(value)
    
    print("entered elements are: ")
    for i in range(length):
        print(arr[i])




if __name__ == "__main__":
    Main()
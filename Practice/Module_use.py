import ModuleX
import Module_Name

def main():
    value1 = int(input("Enter first no.: "))
    value2 = int(input("Enter 2nd no.: "))

    Answer = 0
    Answer = ModuleX.Addition(value1, value2)
    print("Addition is: ", Answer)

    Answer = ModuleX.Subtraction(value1, value2)
    print("Subtraction is: ", Answer)

    Answer = ModuleX.Multiplication(value1, value2)
    print("Multiply is: ", Answer)

    Answer = ModuleX.Division(value1, value2)
    print("Division is: ", Answer)

    print("\nSpecial variable of 2nd imported module is:", Module_Name.DisplayMod)
if __name__ == "__main__":
    main()


"""
This is the demo code to know how modules work and how to use external user-defiend Modules in Py.
"""
from math import pi

circle = lambda x: pi * x * x

sqr = lambda x: x * x

rect = lambda x, y: x * y

tri = lambda x, y: 0.5 * x * y

area_func = {"square": sqr, "rectangle": rect, "triangle": tri, "circle": circle}


def get_number(input_str: str) -> float:
    side = input(input_str)
    num = side.replace(".", "", 1)
    while not num.isdecimal():
        print("Enter a number!!!")
        side = input(input_str)
        num = side.replace(".", "", 1)

    return float(side)


print(
    """
    
      Hello There!!!
      Find the area of the following shapes!!!:
      Rectangle, Circle, Square, Triangle.
      Enter Shape name and find out!!
      
      if you want to leave, enter 'exit'
      Now Let's start!!!
      \n
      """
)


def main():
    while True:
        shape_name = input("Enter Shape name (if you wish to leave enter 'exit'): ")
        match shape_name.lower():
            case "square":
                side = get_number("Enter side of square: ")
                area = area_func["square"]
                print(f"Area of square with side: {side} is: {area(side)}")

            case "rectangle":
                length = get_number("Enter length of rectangle: ")

                breadth = get_number("Enter breadth of rectangle: ")
                area = area_func["rectangle"]
                print(
                    f"Area of rectangle with length: {length} and {breadth} is: {area(length,breadth)}"
                )

            case "circle":
                radius = get_number("Enter radius of circle: ")
                area = area_func["circle"]
                print(f"Area of circle with radius: {radius} is: {area(radius)}")

            case "triangle":
                height = get_number("Enter heighth of triangle: ")

                base = get_number("Enter base of triangle: ")
                area = area_func["triangle"]
                print(f"Area of triangle with height: {height} is: {area(height,base)}")

            case "exit":
                exit()
            case _:
                print("Enter from the cases given!!")


if __name__ == "__main__":
    main()

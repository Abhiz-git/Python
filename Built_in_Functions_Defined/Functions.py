def Split1(String):

    lst = []
    S=""
    String = String.strip()

    for char in String:

        if char != " ":
            S = S+char

        elif char == " ":
            lst.append(S)
            S=""
        
    lst.append(S)

    return lst
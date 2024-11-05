def Split1(String):

    lst = []
    S=""
    String = String.strip()

    for char in String:

        if char != " ":
            S = S+char

        else:
            S = ""
            continue
        
        lst.append(S)


    print(lst)

Split1("Abhi Nale")
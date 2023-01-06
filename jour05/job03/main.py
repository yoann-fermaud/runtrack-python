def draw_carpet(n):
    border = "+"
    for i in range(n + 1):
        border += "-"
    border += "+"
    print(border)

    for i in range(n + 1):
        carpet = ""
        for j in range(n - i):
            carpet += "#"
        carpet += " "
        for j in range(i):
            carpet += "#"
        print(f"|{carpet}|")
    print(border)


draw_carpet(10)

def draw_rectangle(width: int, height: int):
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if j == 1 or j == width:
                print(f"|", end="")
            else:
                if i == 1 or i == height:
                    print(f"-", end="")
                else:
                    print(f" ", end="")
        print()


draw_rectangle(10, 4)

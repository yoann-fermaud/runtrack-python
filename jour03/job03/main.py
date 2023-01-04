def loop():
    for i in range(0, 101):
        if i == 26 or i == 37 or i == 88:
            i += 1
        else:
            print(f'number : {i}')


loop()

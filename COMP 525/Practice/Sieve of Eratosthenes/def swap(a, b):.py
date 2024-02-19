def rev(list):
    if len(list) < 0:
        return
    rev(list[1:])
    print (list[0])

list = (1, 2, 3)

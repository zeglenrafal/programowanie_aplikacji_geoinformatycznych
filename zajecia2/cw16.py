def zmien_wartosc(arg):
    if type(arg) is int:
        arg = 65482652

    elif type(arg) is list:
        arg[0] = 'kalafior'
    else:
        pass
    return arg
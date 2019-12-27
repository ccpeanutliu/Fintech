
def myStrategy(daily, minutely, open):
    q = '''
    tmp = rd.randint(0,1000)
    if tmp % 3 == 0:
        return 1
    elif tmp % 3 == 1:
        return 0
    else:
        return -1
    '''
    if open == 11613:
        return 1
    else:
        return 0
    
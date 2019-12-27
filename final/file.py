import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    arr = []
    for i in range(200,daily.shape[0]):
        avg = np.mean(daily['close'][i-200:i].values)
        arr.append(avg)
    return arr
daily = pd.read_csv("TX_daily.csv")
minutely = pd.read_csv("TX_minutely.csv")

y = myStrategy(daily,minutely, 0)
x = range(0,len(y))

plt.plot(x, y, '-o')
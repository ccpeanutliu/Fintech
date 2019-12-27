import sys
import numpy as np
import pandas as pd
from myStrategy import myStrategy
import time

start = time.time()
dailyOhlcv = pd.read_csv(sys.argv[1])
minutelyOhlcv = pd.read_csv(sys.argv[2])
capital = 500000.0
capitalOrig=capital
transFee = 100
evalDays = 14
action = np.zeros((evalDays,1))
realAction = np.zeros((evalDays,1))
total = np.zeros((evalDays,1))
total[0] = capital
Holding = 0.0
openPricev = dailyOhlcv["open"].tail(evalDays).values
clearPrice = dailyOhlcv.iloc[-3]["close"]

print(evalDays)
for ic in range(evalDays,0,-1):
    dailyOhlcvFile = dailyOhlcv.head(len(dailyOhlcv)-ic)
    dateStr = dailyOhlcvFile.iloc[-1,0]
    minutelyOhlcvFile = minutelyOhlcv.head((np.where(minutelyOhlcv.iloc[:,0].str.split(expand=True)[0].values==dateStr))[0].max()+1)
    action[evalDays-ic] = myStrategy(dailyOhlcvFile,minutelyOhlcvFile,openPricev[evalDays-ic])
    currPrice = openPricev[evalDays-ic]
    if action[evalDays-ic] == 1:
        if Holding == 0 and capital > transFee:
            Holding = (capital-transFee)/currPrice
            capital = 0
            realAction[evalDays-ic] = 1
    elif action[evalDays-ic] == -1:
        if Holding > 0 and Holding*currPrice > transFee:
            capital = Holding*currPrice - transFee
            Holding = 0
            realAction[evalDays-ic] = -1
    elif action[evalDays-ic] == 0:
        realAction[evalDays-ic] = 0
    else:
        assert False
    if ic == 3 and Holding > 0: #遇到每個月的第三個禮拜三要平倉，請根據data的日期自行修改
        capital = Holding*clearPrice - transFee
        Holding = 0

    total[evalDays-ic] = capital + float(Holding>0) * (Holding*currPrice-transFee)


returnRate = (total[-1] - capitalOrig)/capitalOrig
end = time.time()
print("return rate:%f" % returnRate)
print("action:", end=" ")
for i in action:
    print(i[0],end=" ")
print("")
print("total:",end=" ")

for i in total:
    print(i[0],end=" ")
print("")
print(end - start)

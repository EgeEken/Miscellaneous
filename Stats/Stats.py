import math
import statistics

def stats():
    print('Input numbers')
    total = 0.0
    res = []
    change = []
    status = True
    num = 0
    while status:
        num = input()
        if num == 'done':
            status = False
        else:
            try:
                num = float(num)
                total += num
                res.append(num)
            except:
                pass
    for i in range(len(res)-1):
        change.append(res[i+1] - res[i])
    res.sort()
    print('Inputs: ' + str(res))
    print('Total: ' + str(total) + ' Count: ' + str(len(res)))
    print('Average: ' + str(round(statistics.mean(res), 2)))
    if len(res)%2 == 0:
        print('Median: ' + str((res[(len(res)//2 - 1)] + res[(len(res)//2)])/2))
    else:
        print('Median: ' + str(res[(len(res)//2)]))
    print('Average change: ' + str(round(statistics.mean(change), 2)))
    print('Variance: ' + str(round(statistics.variance(res), 2)))
    print('Standard Deviation: ' +str(round(math.sqrt(statistics.variance(res)), 2)))

while True:
    stats()
    a = input()

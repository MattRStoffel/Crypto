#/usr/bin/python3
from PrimeNumber import *
import timeit
import pandas as pd


if __name__ == '__main__':
        
    n = 1000
    table = []

    def addData(x, y):
        s = "randomPrime( " + str(x) + ", " + str(y) + " )"
        time = timeit.timeit(s, globals=globals(), number=n)
        table.append([x, y, time/n, time])
    
    for i in range(10, 200, 20):
        addData(i, 64)
        df = pd.DataFrame(table, columns = ['accuracy', 'size of prime', 'average time', 'total time'] )
        print(df)


    i = 64
    while i <= 1024:
        addData(40, i)
        i += i
        df = pd.DataFrame(table, columns = ['accuracy', 'size of prime', 'average time', 'total time'] )
        print(df)

    
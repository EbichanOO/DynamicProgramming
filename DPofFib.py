# -*- using:utf-8 -*-
import time

def nomal_fib(n: int):
    #初項 = 第0項目とする
    if n < 2:
        return 1
    else:
        return nomal_fib(n-1)+nomal_fib(n-2)

class topDown_fib:
    def __init__(self):
        self.node = [1, 1]
    def __call__(self, n: int):
        if n < len(self.node):
            return self.node[n]
        else:
            A = self.__call__(n-1) + self.__call__(n-2)
            self.node.append(A)
            return self.node[-1]

def bottomUp_fib(n: int):
    if n==0:
        return 1
    else:
        a = b = A = 1
        for i in range(n-1):
            A = a+b
            a = b
            b = A
        return A

def time_measure(i: int):
    TDF = topDown_fib()
    startTime = time.perf_counter()
    nomal_fib(i)
    nomalTime = time.perf_counter()-startTime
    startTime = time.perf_counter()
    TDF(i)
    topDownTime = time.perf_counter()-startTime
    startTime = time.perf_counter()
    bottomUp_fib(i)
    bottomUpTime = time.perf_counter()-startTime
    print(f"nomal fib time : {nomalTime}\ntopDown fib time : {topDownTime}\nbottomUp fib time : {bottomUpTime}\n")

time_measure(19)#20項目まで求めた時間
from collections import *
if __name__ == "__main__":
    n = int(input())
    od = OrderedDict()
    for _ in range(0,n):
        string = input()
        if string in od.keys():
            od[string] += 1
        else:
            od[string] = 1
    print(len(od.keys()))
    for k in od.keys():
        print(od[k], end=' ')
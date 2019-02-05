from collections import *

if __name__ == "__main__":
    od = OrderedDict()

    n = int(input())
    for i in range(0, n):
        line = input()
        line = line.split()
        itemname, price = " ".join(line[:-1]), int(line[-1:][0])
        if itemname in od:
            od[itemname] += price
        else:
            od[itemname] = price
    for k in od.keys():
        print("{} {}".format(k, od[k]))


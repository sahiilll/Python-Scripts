from collections import *
d = defaultdict(list)
n,m = map(int,raw_input().split())
for _ in range(n):
    t = raw_input()
    d[t].append(_+1)
for i in range(m):
    t = raw_input()
    if t in d:
        print " ".join(map(str,d[t]))
    else:
        print -1
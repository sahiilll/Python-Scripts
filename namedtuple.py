from collections import namedtuple
if __name__== "__main__":
    Student = namedtuple('Student', 'p,q,r,s')
    n = int(input())
    p, q, r, s = input().split()
    sum = 0
    if p == "MARKS":
        for i in range(0,n):
            sum = sum + int(input().split()[0])
        print ("{0:.2f}".format(sum/int(n)))
    if q == "MARKS":
        for i in range(0,n):
            sum = sum + int(input().split()[1])
        print ("{0:.2f}".format(sum/int(n)))
    if r == "MARKS":
        for i in range(0,n):
            sum = sum + int(input().split()[2])
        print ("{0:.2f}".format(sum/int(n)))
    if s == "MARKS":
        for i in range(0,n):
            sum = sum + int(input().split()[3])
        print ("{0:.2f}".format(sum/int(n)))




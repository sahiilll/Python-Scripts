from collections import  Counter
if __name__ == "__main__":
    X = input()
    shoe_sizes = input().split(" ")
    avail = Counter(shoe_sizes)

    N = int(input())
    cust = []
    for _ in range(0,N):
        cust.append(input().split(" "))
    print(cust)
    earning = 0
    for i in cust:
        rem = avail.get(str(i[0]))
        if rem != None:

            key = i[0]
            if rem != 0:
                rem = rem - 1
                for j in avail.keys():
                    if j == key:
                        avail[j] = rem
                earning += int((i[1]))
    print(earning)
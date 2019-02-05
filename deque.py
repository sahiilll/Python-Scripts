from collections import  *
if __name__ == "__main__":
    de = deque()

    for _ in range(0, int(input())):
        line = input().split()
        if len(line) == 2:
            method, val = line
        else:
            method = line[0]

        if method == 'append':
            de.append(val)
            #print(" ".join(de))
        elif method == 'appendleft':
            de.appendleft(val)
            #print(" ".join(de))
        elif method == 'pop':
            de.pop()
            #print(" ".join(de))
        elif method == 'popleft':
            de.popleft()
            #print(" ".join(de))

    print(" ".join(de))




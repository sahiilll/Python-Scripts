from collections import *
if __name__ == "__main__":
    cubes = deque()

    def check(cubes):
        if

    for _ in range(0, int(input())):
        n = int(input())

        cubes = input().split()
        last = cubes.pop()
        for _ in cubes:
            if last >= cubes[len(cubes) - 1]:
                last = cubes.pop()
            elif last >= cubes[0]:
                last = cubes.popleft()
            else:
                print("No")
                exit(0)
        print("Yes")










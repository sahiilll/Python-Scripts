def getleft(index):
    return index * 2
def getright(index):
    return index * 2 + 1
def min_heapify(arr, i):
    left = getleft(i)
    right = getright(i)
    smallest = i
    if (len(arr) > left) and (arr[left] < arr[i]):
        smallest = left
    if(len(arr) > right) and (arr[right] < arr[i]):
        smallest = right
    if(i != smallest):
        swap(arr,smallest,i)
        min_heapify(arr,smallest)
def swap(arr,i1,i2):
    flag = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = flag
def Add(ele, arr):
    arr.append(ele)
    for x in range(int(len(arr)/2),-1,-1):
        min_heapify(arr,x)
def Delete(ele,arr):
    swap(arr,arr.index(ele),len(arr) - 1)
    arr.remove(arr[len(arr) - 1])
    for x in range(int(len(arr)/2),-1,-1):
        min_heapify(arr,x)
def Minimum(arr):
    return arr[0]
if __name__ == '__main__':
    x =  int(input())
    arr = []
    for _ in range(x):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            Add(inp[1],arr)
            print(arr)
        elif inp[0] == 2:
            Delete(inp[1], arr)
            print(arr)
        elif inp[0] == 3:
            print("Minimum = ", Minimum(arr))
        else:
            raise Exception

def merge_the_tools(string, k):
    # your code goes here
    words = []
    result = []
    for i in range(0,len(string),k):
        words.append(string[i:i+k])
    for s in words:
        result.append(''.join(sorted(set(s), key=s.index)))
    for i in result:
        print(i)
    a, b = [1, 2]
    print(a)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
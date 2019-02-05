import textwrap

def wrap(string, max_width):
    l = list(string)
    string1 = ""
    for i in range(0,len(string),max_width):

        string = "".join(l[i:i + max_width])
        string1 += string + "\n"

    return string1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print (result)
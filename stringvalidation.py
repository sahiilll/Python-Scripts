# alpanum
# alpha
# digit
# lower
# upper
if __name__ == '__main__':

    s = raw_input()
    flag = False
    for i in range(0, len(s)):
        if s[i].isalpha() or s[i].isdigit():
            print
            True
            flag = True
            break
    if flag == False:
        print
        False
    flag = False
    for i in range(0, len(s)):
        if s[i].isalpha():
            print
            True
            flag = True
            break
    if flag == False:
        print
        False

    flag = False
    for i in range(0, len(s)):
        if s[i].isdigit():
            print
            True
            flag = True
            break
    if flag == False:
        print
        False
    flag = False
    for i in range(0, len(s)):
        if s[i].islower():
            print
            True
            flag = True
            break
    if flag == False:
        print
        False
    flag = False
    for i in range(0, len(s)):
        if s[i].isupper():
            print
            True
            flag = True
            break
    if flag == False:
        print
        False


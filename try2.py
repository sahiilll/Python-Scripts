#finding number of same substrings

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        flag = False
        if string[i] == sub_string[0]:
            pos = i

            for j in range(0, len(sub_string)):
                #acdprint(pos)
                if sub_string[j] == string[pos]:
                    flag = True
                    if pos != len(string) - 1:
                        pos = pos + 1
                    #print("{} {}".format(pos, j))
                else:
                    flag = False
                    break
               # print("{} {} {}".format(flag, i,j))
            if flag == True:
                count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print (count)
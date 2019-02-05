
if __name__ == '__main__':
    string = input()
    list_of_kevin = []
    list_of_stuart = []
    score_kevin = 0
    score_stuart = 0
    for i in range(0,len(string)):
        if "aeiouAEIOU".find(string[i]) != -1:
            list_of_kevin.append(i)
        else:
            list_of_stuart.append(i)
    #print(list_of_stuart)
    #print(list_of_kevin)
    for i in range(0,len(list_of_kevin)):
        score_kevin += len(string) - list_of_kevin[i]
    for i in range(0,len(list_of_stuart)):
        score_stuart += len(string) - list_of_stuart[i]

    if score_kevin > score_stuart:
        print ("kevin {}".format(score_kevin))
    else:
        print("Stuart {}".format(score_stuart))


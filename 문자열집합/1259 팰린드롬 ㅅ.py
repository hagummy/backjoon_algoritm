while True:
    word=input()
    if word=='0':
        break
    flag=True
    for i in range(0,len(word)//2):
        if word[i]!=word[len(word)-i-1]:
            flag=False
            break
    if flag==True:
        print("yes")
    else:
        print("no")
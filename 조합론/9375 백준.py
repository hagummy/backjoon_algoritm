from collections import Counter
tc=int(input())
for _ in range(tc): #test case만큼 진행
    n=int(input()) #의상 갯수
    wear=[] #의상을 넣을 곳
    for _ in range(n):
        a,b=input().split()
        wear.append(b)
    wear_dict=Counter(wear)
    cnt=1 #answer
    for key in wear_dict:
        cnt*=(wear_dict[key]+1)
    print(cnt-1)
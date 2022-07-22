from collections import defaultdict
tc=int(input())
for _ in range(tc): #test case만큼 진행
    n=int(input()) #의상 갯수
    weardict=defaultdict(list) #의상을 넣을 곳
    for _ in range(n):
        a,b=input().split()
        weardict[b].append(a)
    cnt=1 #answer
    for key in weardict:
        cnt*=(len(weardict[key])+1)
    print(cnt-1)
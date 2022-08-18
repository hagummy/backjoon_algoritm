n=int(input())
lst=list(map(int,input().split()))
lst.sort()
cnt=0
num=lst[-1]
canfind=[True]*(num+1)
canfind[1]=False
for i in range(2,num//2+1):
    for j in range(2,num//i+1):
        canfind[i*j]=False
print(canfind)       
for i in lst:
    if canfind[i]==True:
        cnt+=1
print(cnt)
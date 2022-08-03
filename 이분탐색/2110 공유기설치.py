from sys import stdin
input=stdin.readline
n,c=map(int,input().split())
home=[]
for _ in range(n):
    home.append(int(input()))
home.sort() #오름차순으로 
start=1
end=home[-1]-home[0]
answer=0

while start<=end:
    mid=(start+end)//2
    count=1
    ts=home[0]
    for i in range(1,n):
        if home[i]-ts>=mid:
            count+=1
            ts=home[i]
    if count>=c:
        start=mid+1
        answer=mid
    else:
        end=mid-1
print(answer)
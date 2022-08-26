import sys
input=sys.stdin.readline
n=int(input())
pn='I'
for _ in range(n):
    pn+='OI'
m=int(input())
s=input()
answer=0
l=2*n+1
for i in range(0,m):
    if s[i:i+l]==pn:
        answer+=1
print(answer)
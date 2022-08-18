import sys
input=sys.stdin.readline
n,m=map(int,input().split())
nohear=set()
nosee=set()
print(nohear)
for _ in range(n):
    temp=input().rstrip()
    nohear.add(temp)
for _ in range(m):
    temp=input().rstrip()
    nosee.add(temp)
print(nohear)
nohearsee=list(nohear.intersection(nosee))
print(len(nohearsee))
for i in nohear:
    print(i)

n,m=map(int,input().split())
nohear=set()
nosee=set()
for _ in range(n):
    nohear.add(input())
for _ in range(m):
    nosee.add(input())
both=list[nohear.intersection(nohear)]
print(both)
print(len(both))
for name in both:
    print(name)
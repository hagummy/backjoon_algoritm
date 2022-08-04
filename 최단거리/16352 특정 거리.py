import sys
from collections import deque
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
cango=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    cango[a].append(b)

q=deque([x])
visited=[-1]*(n+1)
visited[x]=0
while q:
    city=q.popleft()
    for nextcity in cango[city]:
        if visited[nextcity]==-1:
            visited[nextcity]=visited[city]+1
            q.append(nextcity)
            
flag=False
for i in range(1,n+1):
    if visited[i]==k:
        flag=True
        print(i)
if flag==False:
    print(-1)
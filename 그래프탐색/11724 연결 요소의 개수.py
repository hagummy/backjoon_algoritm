import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
con=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    con[x].append(y)
    con[y].append(x)
visited=[0]*(n+1)
print(con)
q=deque()
answer=[]
for i in range(1,n+1):
    if visited[i]==0:
        q.append(i)
        visited[i]=1
        lst=[i]
        while q:
            now=q.popleft()
            for i in con[now]:
                if visited[i]==0:
                    lst.append(i)
                    visited[i]=1
                    q.append(i)
        answer.append(lst)
                    
print(len(answer))   
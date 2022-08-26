from collections import deque
n,m,v=map(int,input().split())
lst=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)
for i in range(len(lst)):
    lst[i].sort()

def dfs(num,cnt,answer):

    if cnt==n:
        return
    print(num,end=' ')
    
    for i in lst[num]:
        if i not in answer:
            answer.append(i)
            dfs(i,cnt+1,answer)

    
    
def bfs(num):
    print(num,end=' ')
    q=deque()
    q.append(num)
    visited=[0]*(n+1)
    visited[num]=1
    while q:
        now=q.popleft()
        for i in lst[now]:
            if visited[i]==0:
                print(i,end=' ')
                visited[i]=1
                q.append(i)
                
dfs(v,0,[v])
print()
bfs(v)
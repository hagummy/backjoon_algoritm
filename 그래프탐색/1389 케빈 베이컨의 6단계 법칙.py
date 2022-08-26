from collections import deque
n,m=map(int,input().split())
lst=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)
answer=[]
def bfs(start):
    visited=[-1]*(n+1)
    q=deque([start])
    visited[start]=0
    while q:
        friend=q.popleft()
        for i in lst[friend]:
            if visited[i]==-1:
                visited[i]=visited[friend]+1
                q.append(i)
    return(sum(visited)+1)
for i in range(1,n+1):
    kevin=bfs(i)
    answer.append([i,kevin])
answer.sort(key=lambda x:(x[1],x[0]))
print(answer[0][0])
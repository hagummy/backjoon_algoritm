from collections import deque
n=int(input())
adj=[[] for _ in range(n+1)]
while True:
    m1,m2=map(int,input().split())
    if m1==-1 and m2==-1:
        break
    adj[m1].append(m2)
    adj[m2].append(m1)
def bfs(N):
    visited=[-1]*(n+1)
    visited[N]=0
    q=deque([N])
    while q:
        v=q.popleft()
        for w in adj[v]:
            print(w)
            if visited[w]==-1:
                visited[w]=visited[v]+1
                q.append(w)
    return max(visited)
score=50

for i in range(1,n+1):
    temp=bfs(i)
    if temp<score:
        score=temp
        lst=[i]
    elif temp==score:
        lst.append(i)
print(score,len(lst))
print(' '.join(map(int,lst)))
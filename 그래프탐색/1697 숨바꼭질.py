from collections import deque
n,k=map(int,input().split())
visited=[-1]*(100001)

q=deque()
q.append(n)
visited[n]=0
while q:
    now=q.popleft()
    if now==k:
        print(visited[k])
        break
    for x in [now-1,now+1,2*now]:
        if 0<=x<=100000:
            if visited[x]==-1:
                visited[x]=visited[now]+1
                q.append(x)
                print(q)
    

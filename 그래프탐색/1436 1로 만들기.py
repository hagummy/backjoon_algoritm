from collections import deque
n=int(input())
max=1000000
q=deque()
q.append(n)
visited=[-1]*(max+1)
visited[n]=0
while q:
    x=q.popleft()
    if x==1:
        print(visited[1])
        break
    if x%3==0:
        if 0<=x//3<=max and visited[x//3]==-1:
            q.append(x//3)
            visited[x//3]=visited[x]+1
    if x%2==0:
        if 0<=x//2<=max and visited[x//2]==-1:
            q.append(x//2)
            visited[x//2]=visited[x]+1
    if 0<=x-1<=max and visited[x-1]==-1:
        q.append(x-1)
        visited[x-1]=visited[x]+1
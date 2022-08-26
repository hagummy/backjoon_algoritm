import sys
input=sys.stdin.readline
from collections import deque
m,n=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,-1,0,1]
visited=[[-1]*(m) for _ in range(n)]
q=deque()
answer=-1
tomato=[0,0,0]
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            q.append([i,j])
            visited[i][j]=0
            tomato[0]+=1
            tomato[1]+=1
        elif board[i][j]==0:
            tomato[0]+=1
            tomato[2]+=1
if tomato[0]==tomato[1]:
    print(0)
    exit()
            
while q:
    for i in range(len(q)):
        r,c=q.popleft()
        for j in range(4):
            nr,nc=r+dr[j],c+dc[j]
            if 0<=nr<n and 0<=nc<m:
                if board[nr][nc]==0 and visited[nr][nc]==-1:
                    visited[nr][nc]=0
                    board[nr][nc]=1
                    q.append([nr,nc])
                    tomato[2]-=1
                    tomato[1]+=1
    answer+=1
if tomato[0]==tomato[1]:
    print(answer)
else:
    print(-1)
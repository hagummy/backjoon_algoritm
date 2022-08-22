import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().rstrip())) for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,-1,0,1]
q=deque()
q.append([0,0,0])
visited=[[[-1]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1
answer=False
while q:
    r,c,flag=q.popleft()
    if r==n-1 and c==m-1:
        print(visited[r][c][flag])
        answer=True
        break
    for i in range(4):
        nr,nc=r+dr[i],c+dc[i]
        if nr<0 or nr>=n or nc<0 or nc>=m:
            continue
        if visited[nr][nc][flag]==-1 and board[nr][nc]==0:
            visited[nr][nc][flag]=visited[r][c][flag]+1
            q.append([nr,nc,flag])
        elif board[nr][nc]==1 and flag==0:
            visited[nr][nc][1]=visited[r][c][0]+1
            q.append([nr,nc,1])
if answer==False:
    print(-1)
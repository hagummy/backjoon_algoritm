import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().rstrip())) for _ in range(n)]
print(board)
visited=[[-1]*m for _ in range(n)]
q=deque([[0,0]])
visited[0][0]=1
dr=[-1,0,1,0]
dc=[0,-1,0,1]
while q:
    r,c=q.popleft()
    if r==n-1 and c==m-1:
        print(visited[r][c])
        break
    for i in range(4):
        nr,nc=r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m:
            if board[nr][nc]==1 and visited[nr][nc]==-1:
                visited[nr][nc]=visited[r][c]+1
                q.append([nr,nc])
    
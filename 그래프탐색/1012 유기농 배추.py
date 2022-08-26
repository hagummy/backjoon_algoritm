import sys
from collections import deque
input=sys.stdin.readline
tc=int(input())
dr=[-1,0,1,0]
dc=[0,-1,0,1]
for _ in range(tc):
    answer=0
    m,n,k=map(int,input().split())
    board=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for _ in range(k):
        c,r=map(int,input().split())
        board[r][c]=1
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and visited[i][j]==0:
                q=deque()
                q.append([i,j])
                visited[i][j]=1
                while q:
                    r,c=q.popleft()
                    for k in range(4):
                        nr,nc=r+dr[k],c+dc[k]
                        if 0<=nr<n and 0<=nc<m and board[nr][nc]==1:
                            if visited[nr][nc]==0:
                                q.append([nr,nc])
                                visited[nr][nc]=1

                answer+=1          
    print(answer)    

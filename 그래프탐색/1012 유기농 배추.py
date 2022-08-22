from collections import deque
import sys
input=sys.stdin.readline
dr=[-1,0,1,0]
dc=[0,-1,0,1]
def bfs(r,c):
    global m,n
    temp=[[r,c]]
    q=deque()
    q.append([r,c])
    visited[r][c]=1
    while q:
        r,c=q.popleft()
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<m:
                if board[nr][nc]==1 and visited[nr][nc]==0:
                    visited[nr][nc]=1
                    q.append([nr,nc])
                    temp.append([nr,nc])
    return temp   
tc=int(input())
for _ in range(tc):
    m,n,k=map(int,input().split())
    board=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        board[y][x]=1
    
    answer=[]
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and visited[i][j]==0 :
                answer.append(bfs(i,j))
                
    print(len(answer))
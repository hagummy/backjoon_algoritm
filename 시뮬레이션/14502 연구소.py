import sys
from collections import deque
from copy import deepcopy
input=sys.stdin.readline

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
answer=0
def count_safe():
    global answer
    new_board=deepcopy(board)
    dr=[-1,0,1,0]
    dc=[0,-1,0,1]
    q=deque()
    cnt=0
    for i in range(n):
        for j in range(m):
            if new_board[i][j]==2:
                q.append((i,j))
    while q:
        r,c=q.popleft()
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<m:
                if new_board[nr][nc]==0:
                    new_board[nr][nc]=2
                    q.append((nr,nc))
    for i in range(n):
        cnt+=new_board[i].count(0)
        
    
    answer=max(answer,cnt)
    print(answer)
    return                             
                    
                
    
    
def make_wall(cnt):
    global answer
    if cnt==3:
        count_safe()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                make_wall(cnt+1)
                board[i][j]=0

make_wall(0)
print(answer)
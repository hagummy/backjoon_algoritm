from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
move=[(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start_r,start_c):
    visited=[[-1 for _ in range(m)] for _ in range(n)]
    q=deque([(start_r,start_c)])
    visited[start_r][start_c]=0
    
    while q:
        nr,nc=q.popleft()
        for dr,dc in move:
            r,c=nr+dr,nc+dc
            if (0<=r<n and 0<=c<m):
                if board[r][c]==1 and visited[r][c]==-1:
                    visited[r][c]=visited[nr][nc]+1
                    q.append([r,c])
                elif board[r][c]==0:
                    visited[r][c]=0
    return visited

for i in range(n):
    for j in range(m):
         if board[i][j]==2:
            answer=bfs(i,j)
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print(0,end=' ')
        else:
            print(answer[i][j],end=' ')
    print()
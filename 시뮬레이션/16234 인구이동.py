from collections import deque
n,L,R = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,-1,0,1]

def bfs(i,j):
    q=deque() #큐 생성
    q.append([i,j])
    visited[i][j]=1
    temp=[[i,j]]
    while q:
        nr,nc=q.popleft()
        for i in range(4):
            r,c=nr+dr[i],nc+dc[i]
            if (0<=r<n and 0<=c<n and visited[r][c]==0 ):
                if L <= abs(board[nr][nc] - board[r][c]) <= R:  
                    q.append([r,c])
                    visited[r][c]=1
                    temp.append([r,c])
    return temp
cnt=0
while True:
    flag=False
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                temp=bfs(i,j)
                if len(temp)>1:
                    flag=True
                    people=sum(board[x][y] for x,y in temp)//len(temp)
                    for r,c in temp:
                        board[r][c]=people
    if flag==False:
        break
    cnt+=1

print(cnt)
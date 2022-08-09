from collections import deque
n,m,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,-1,0,1]
visited=[[-1 for _ in range(m)] for _ in range(n)]

q=deque([(0,0)])
visited[0][0]=0
answer=0
while q:
    nr,nc=q.popleft()
    if (nr==n-1 and nc==m-1): #끝날 조건
        if answer:
            answer=min(answer,visited[nr][nc])
            break
        else:
            answer=visited[nr][nc]
            break
            
    for i in range(4):
        r,c=nr+dr[i],nc+dc[i]       
        if (0<=r<n and 0<=c<m and visited[r][c]==-1):
            if board[r][c]==1:
                continue
            visited[r][c]=visited[nr][nc]+1
            q.append([r,c])
            if board[r][c]==2:
                answer=visited[r][c]+abs(n-r-1)+abs(m-c-1)

if 0<answer<=t:
    print(answer)
else:
    print("Fail")
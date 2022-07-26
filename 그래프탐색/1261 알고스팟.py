from collections import deque
m,n=map(int,input().split()) #m:가로 n:세로
miro=[list(map(int,input())) for _ in range(n)] #해쳐나아가아햘 미로
nr,nc=0,0 #현재 위치
dr=[-1,0,1,0] #방향 정보
dc=[0,-1,0,1]
visited=[[-1]*m for _ in range(n)]
visited[0][0]=0
q=deque() 
q.append([0,0]) #r좌표,c좌표,벽부슨횟수
while q: #큐 존재할 때
    nr,nc=q.popleft() #뽑기
    for i in range(4): #방향 살피기
        r,c=nr+dr[i],nc+dc[i] 
        if (0<=r<n and 0<=c<m): #범위 안에 존재
            if visited[r][c]==-1: #벽이 존재하면
                if miro[r][c]==0:
                    visited[r][c]=visited[nr][nc]
                    q.appendleft([r,c])
                else:
                    visited[r][c]=visited[nr][nc]+1
                    q.append([r,c])

print(visited[n-1][m-1])

from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)] #구름판
move=[] #이동 방향, 횟수
for _ in range(m):
    d,s=map(int,input().split())
    move.append([d,s])
dir=[[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]] #방향 서쪽부터 시계방향
temp=[]
cloud=deque() #구름 저장
cloud.append([n-1,0])
cloud.append([n-1,1]) #초기 구름 
cloud.append([n-2,0])
cloud.append([n-2,1])
answer=0

def wind_blow(d,s,visited): #구름 이동 함수
    dr,dc=dir[d] #행, 열 방향
    for _ in range(len(cloud)): #저장된 구름만큼
        r,c=cloud.popleft()
        for j in range(s):
            r+=dr
            c+=dc
            if r<0:
                r=n-1
            elif r>=n:
                r=0
            if c<0:
                c=n-1
            elif c>=n:
                c=0
        board[r][c]+=1 #물의 양 1 증가
        temp.append([r,c]) #구름 임시 저장
        visited[r][c]=True
 
    for nr,nc in temp: 
        cnt=0
        for i in [2,4,6,8]:
            dr,dc=dir[i] #비 양 증가
            r,c=nr+dr,nc+dc
            if 0<=r<n and 0<=c<n:
                if board[r][c]>0:
                    cnt+=1
        board[nr][nc]+=cnt
    return visited

def make_cloud(visited):
    for i in range(n):
        for j in range(n):
            if board[i][j]>=2:
                if not visited[i][j]:
                    cloud.append([i,j])
                    board[i][j]-=2

for i in range(m): #횟수만큼
    visited=[[False]*n for _ in range(n)]
    d,s=move[i]
    wind_blow(d,s,visited)
    make_cloud(visited)
    temp=[]
    
for i in range(n):
    answer+=sum(board[i])
print(answer)
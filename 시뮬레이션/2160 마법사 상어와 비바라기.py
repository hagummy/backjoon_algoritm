import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
dr=[0,0,-1,-1,-1,0,1,1,1]
dc=[0,-1,-1,0,1,1,1,0,-1]
board=[list(map(int,input().split())) for _ in range(n)]
di=[] #이동 정보
for _ in range(m):
    x,y=map(int,input().split())
    di.append([x,y])
cloud=deque() #구름 저장
cloud.append([n-1,0])
cloud.append([n-1,1]) #초기 구름 
cloud.append([n-2,0])
cloud.append([n-2,1])
answer=0

def move(dir,cnt,visited):
    temp=[]
    for _ in range(len(cloud)):
        r,c=cloud.popleft()
        for _ in range(cnt):
            r+=dr[dir]
            if r<0: r=n-1
            elif r>=n: r=0
            c+=dc[dir]
            if c<0: c=n-1
            elif c>=n: c=0
        board[r][c]+=1
        temp.append([r,c])
    for r,c in temp: #물 증가
        num=0
        for i in [2,4,6,8]:
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<n:
                if board[nr][nc]>0:
                    num+=1
        board[r][c]+=num

    for i in range(n):
        for j in range(n):
            if board[i][j]>=2 and [i,j] not in temp:
                cloud.append([i,j])
                board[i][j]-=2
for dir,cnt in di:
    move(dir,cnt)
for i in range(n):
    answer+=sum(board[i])
print(answer)
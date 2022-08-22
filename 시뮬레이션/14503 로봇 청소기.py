import sys
input=sys.stdin.readline

n,m=map(int,input().split())
move=[(-1,0),(0,1),(1,0),(0,-1)]
rr,rc,rd=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

def clean(r,c,d):
    global n,m
    cnt=1
    while True:
        temp=0
        for i in range(4):
            mr,mc=r+move[(3+d-i)%4][0],c+move[(3+d-i)%4][1]
            if 0<=mr<n and 0<=mc<m:
                if board[mr][mc]==0: #왼쪽 방향에 청소하지 않은 공간이 존재한다면
                    board[mr][mc]=2 #청소를 시키고
                    r,c=mr,mc #위치를 변경하고
                    d=(3+d-i)%4 #청소기 방향을 변경하고
                    cnt+=1 #청소 횟수를 추가한다
                    break
            temp+=1
        if temp==4:
            nr,nc=r+move[(d+2)%4][0],c+move[(d+2)%4][1]
            if board[nr][nc]==1:
                return cnt
            else:
                r,c=nr,nc
           
                    
board[rr][rc]=2              
print(clean(rr,rc,rd))
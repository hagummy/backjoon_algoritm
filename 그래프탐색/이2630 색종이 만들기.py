import sys
input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
result=[0,0]
def count(r,c,n):
    color=board[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if board[i][j]!=color:
                count(r,c,n//2)
                count(r+n//2,c,n//2)
                count(r,c+n//2,n//2)
                count(r+n//2,c+n//2,n//2)
                return
    if color==0:
        result[0]+=1
    else:
        result[1]+=1
count(0,0,n)
for i in result:
    print(i)
import sys
input=sys.stdin.readline
n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
num=[0,0,0]
def count(n,board):
    color=board[0][0]
    flag=True
    for i in range(n):
        for j in range(n):
            if board[i][j]!=color:
                flag=False
                break
    if flag==True:
        if color==-1:
            num[0]+=1
        elif color==0:
            num[1]+=1
        elif color==1:
            num[2]+=1
    else:
        for i in range(0,n,n//3):
            for a in range(0,n,n//3):
                temp=[[0]*(n//3) for _ in range(n//3)]
                for j in range(0,n//3):
                    for b in range(0,n//3):
                        temp[j][b]=board[i+j][a+b]
                count(n//3,temp)

count(n,paper)
for i in num:
    print(i)
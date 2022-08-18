import sys
input=sys.stdin.readline
n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
white_paper=0
blue_paper=0
visited=[[0]*n for _ in range(n)]
def count(paper,n):
    global white_paper,blue_paper
    color=paper[0][0]
    for i in range(n):
        for j in range(n):
            if paper[i][j]!=color:
                return False
    if color==1:
        blue_paper+=1
    else:
        white_paper+=1
    return True
N=n   
n=n*2  
while True:    
    for x in range(0,N,n//2):
        for a in range(0,N,n//2):
            temp=[[0]*(n//2) for _ in range(n//2)]
            flag=True
            for y in range(0,n//2):
                for b in range(0,n//2):
                    if visited[x+y][a+b]==0:
                        temp[y][b]=board[x+y][a+b]
                    else:
                        flag=False
            if flag==True:            
                if count(temp,n//2):
                    for i in range(0,n//2):
                        for j in range(0,n//2):
                            visited[x+i][a+j]=1
    n=n//2
    if n==1:
        break
print(white_paper)
print(blue_paper)
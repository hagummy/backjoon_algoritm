n,m,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)] #추가해야할 양분
af=[[5]*n for _ in range(n)] #초기 양분
board=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int,input().split())
    board[x-1][y-1].append(z)
move=[[-1,-1],(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def spring_summmer():
    for i in range(n):
        for j in range(n):
            if board[i][j]!=[]: #나무가 존재한다면
                board[i][j].sort() #어린 나무부터
                temp=[]
                dead=0
                for k in range(len(board[i][j])):
                    if board[i][j][k]<=af[i][j]:
                        af[i][j]-=board[i][j][k]
                        temp.append(board[i][j][k]+1)  
                    else:
                        dead+=(board[i][j][k])//2
                af[i][j]+=dead
                board[i][j]=[]    
                board[i][j].extend(temp)
 

    for i in range(n):
        for j in range(n):
            print(i,j)
            if board[i][j]:
                for age in board[i][j]:
                    if age%5==0:
                        for i in range(8):
                            dr,dc=move[i]
                            nr,nc=i+dr,j+dc
                            if (0<=nr<n and 0<=nc<n):
                                board[nr][nc].append(1)
def winter():
    for i in range(n):
        for j in range(n):
            af[i][j]+=a[i][j]
            
for _ in range(k):
    spring_summmer()
    winter()
answer=0

for i in range(n):
    for j in range(n):
        if board[i][j]!=[]:
            answer+=len(board[i][j])
print(answer)
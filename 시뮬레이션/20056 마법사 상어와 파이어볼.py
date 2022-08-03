n,m,k=map(int,input().split())
board=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r,c,m,s,d=map(int,input().split())
    board[r-1][c-1].append([m,s,d])
di=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] #이동 북쪽부터 시계
answer=0

def move():
    global board
    temp=[[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for b in range(len(board[i][j])):
                m,s,d= board[i][j][b]
                r,c=i,j
                for _ in range(s):
                    r,c=r+di[d][0],c+di[d][1]
                    if r<0: r=n-1
                    elif r>=n: r=0
                    if c<0: c=n-1
                    elif c>=n: c=0
                temp[r][c].append([m,s,d])    
                       
    board=[[[] for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if len(temp[i][j])>=2:
                ma,sa,do,de=0,0,0,0
                for b in range(len(temp[i][j])):
                    ma+=temp[i][j][b][0]
                    sa+=temp[i][j][b][1]
                    if temp[i][j][b][2]%2==0:
                        de+=1
                    else:
                        do+=1
                ma=ma//5
                sa=sa//len(temp[i][j])
                if ma>0:
                    if de==len(temp[i][j]) or do==len(temp[i][j]): #모두 짝수나 홀수
                        for q in [0,2,4,6]:
                            board[i][j].append([ma,sa,q])
                    else:
                        for q in [1,3,5,7]:
                            board[i][j].append([ma,sa,q])

            elif temp[i][j]!=[]:
                m,s,d=temp[i][j][0]
                if m>0:
                    board[i][j].append([m,s,d])
for _ in range(k):
    move()
    
for i in range(n):
    for j in range(n):
        if board[i][j]!=[]:
            for b in range(len(board[i][j])):
                answer+=board[i][j][b][0]
print(answer)
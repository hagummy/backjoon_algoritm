n,m=map(int,input().split())
board=[]
for _ in range(n):
    board.append(input())
mini=[]
for a in range(n-7):
    for i in range(m-7):
        idx1,idx2=0,0
        for b in range(a,a+8):
            for j in range(i,i+8):
                if (j+b)%2==0:
                    if board[b][j] != 'W': idx1 += 1  
                    if board[b][j] != 'B': idx2 += 1
                else :
                    if board[b][j] != 'B': idx1 += 1
                    if board[b][j] != 'W': idx2 += 1
        mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        mini.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(mini))                                 
                    
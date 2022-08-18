n,m=map(int,input().split())
board=[[0 for _ in range(n)] for _ in range(n)]
word=[]
answer=[]
for _ in range(n):
    word.append(input())
for i in range(n):
    for j in range(i,n):
        cnt=0
        for k in range(m):
            if word[i][k]!=word[j][k]:
                cnt+=1
        board[i][j]=board[j][i]=cnt
for i in range(n):
    answer.append((i,sum(board[i])))
    
answer.sort(key=lambda x : (x[1],x[0]))
print(board)
for i in range(n):
    if answer[i][1]==answer[0][1]:
        print(word[answer[i][0]])
    else:
        print(answer[0][1])
        break
                
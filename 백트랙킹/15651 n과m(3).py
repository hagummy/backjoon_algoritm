n,m=map(int,input().split())

def backtracking(cnt,li):
    if cnt==m:
        print(' '.join(map(str,li)))
        return
        
    for i in range(1,n+1):
        li.append(i)
        backtracking(cnt+1,li)
        li.pop()
        
for i in range(1,n+1):
    li=[i]
    backtracking(1,li)
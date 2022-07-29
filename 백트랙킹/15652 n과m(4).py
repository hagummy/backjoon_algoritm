n,m=map(int,input().split())

def backtracking(st,cnt,li):
    if cnt==m:
        print(' '.join(map(str,li)))
        return
        
    for i in range(st,n+1):
        li.append(i)
        backtracking(i,cnt+1,li)
        li.pop()
        
for i in range(1,n+1):
    li=[i]
    backtracking(i,1,li)
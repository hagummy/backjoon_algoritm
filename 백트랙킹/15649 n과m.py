n,m=map(int,input().split())

def backtracking(cnt,num):
    if cnt==m:
        print(' '.join(map(str,num)))
    for i in range(1,n+1):
        if i in num:
            continue
        num.append(i)
        backtracking(cnt+1,num)
        num.pop()

for i in range(1,n+1):
    backtracking(1,[i])
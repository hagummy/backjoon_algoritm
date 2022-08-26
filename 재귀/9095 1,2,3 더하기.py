import sys
input=sys.stdin.readline
tc=int(input())
def dfs(t):
    global cnt,n
    if t>=n:
        if t==n:
            cnt+=1
        return 

    dfs(t+1)
    dfs(t+2)
    dfs(t+3)
    
for _ in range(tc):
    n=int(input())
    cnt=0
    dfs(0)
    print(cnt)
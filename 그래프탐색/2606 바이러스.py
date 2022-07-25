from collections import deque
n=int(input()) #컴퓨터의 수
connect=int(input()) #연결되어있는 컴퓨터
q=deque() #연결된 컴퓨터
board=[[] for _ in range(n+1)] #연결된 컴퓨터
for _ in range(connect):
    a,b=map(int,input().split())
    board[a].append(b)
    board[b].append(a)
visited=[0]*(n+1)

def dfs(board,v,visited):
    visited[v]=1
    for i in board[v]:
        if visited[i]==0:
            dfs(board,i,visited)
    return True
dfs(board,1,visited)
print((sum(visited))-1)

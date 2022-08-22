n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dfs(x,y):
    for a,b in graph[x]:
        if visited[a]==-1:
            visited[a]=y+b
            dfs(a,y+b)
visited=[-1]*(n+1)
visited[1]=0
dfs(1,0)
print(visited)
start=visited.index(max(visited))
print(start)
visited=[-1]*(n+1)
visited[start]=0
dfs(start,0)
print(visited)
print(max(visited))
    
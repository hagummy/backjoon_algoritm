from collections import deque

def bfs(n,i,computers):
    visited=[0]*(n+1)
    q=deque([i])
    visited[i]=1
    answer=[i]
    while q:
        now=q.popleft()
        for next in range(n):
            if computers[now][next]==1 and now!=next:
                if visited[next]==0:
                    q.append(next)
                    visited[next]=1
                    answer.append(next)
    
    return answer
    
def solution(n, computers):
    answer=0
    networks=[]
    for i in range(n):
        if i not in networks:
            network=bfs(n,i,computers)
            networks.extend(network)    
            answer+=1
    return answer
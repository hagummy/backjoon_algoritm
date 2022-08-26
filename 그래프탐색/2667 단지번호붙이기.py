from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*(n) for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,-1,0,1]
answer=[]
def bfs(r,c):
    q=deque([[r,c]])
    visited[r][c]=1
    cnt=1
    while q:
        nr,nc=q.popleft()
        for i in range(4):
            rr,rc=nr+dr[i],nc+dc[i]
            if 0<=rr<n and 0<=rc<n and board[rr][rc]==1:
                if visited[rr][rc]==0:
                    visited[rr][rc]=1
                    cnt+=1
                    q.append([rr,rc])
    return cnt

for i in range(n):
    for j in range(n):
        if board[i][j]==1 and visited[i][j]==0:
            answer.append(bfs(i,j))
answer.sort()
for num in answer:
    print(num)
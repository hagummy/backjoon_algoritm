board = [list(map(int, input())) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
domino = [[False] * 7 for _ in range(7)]

def find(r,c):
    if r==8: 
        return 1 #종료 조건
    count=0
    nr,nc=r,c+1 #가로 탐색
    if nc==7: #끝 행
        nr,nc=r+1,0 #다음줄로 이동
    if visited[r][c]: #이미 방문하였다면
        return find(nr,nc) #다음 탐색
    else:
        now=board[r][c] #현재 위치에 적힌 수
        visited[r][c]=True #방문 응
        for dr,dc in ((0,1),(1,0)): #가로 세로 탐색
            mr,mc=r+dr,c+dc
            if (0<=mr<8 and 0<=mc<7) : #범위안에 존재하면
                pair=board[mr][mc] #다음 위치에 적힌 수
                if not visited[mr][mc] and not domino[now][pair]: #방문한 적 없고 도미노 사용한 적 없음
                    visited[mr][mc]=True #방문 응
                    domino[now][pair]=domino[pair][now]=True #방문 응
                    count+=find(nr,nc)
                    visited[mr][mc]=False #방문 취소
                    domino[now][pair]=domino[pair][now]=False #방문 취소
                    
    visited[r][c]=False
    return count

print(find(0,0))
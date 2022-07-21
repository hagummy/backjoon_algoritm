n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1
max_vol=-1

for i in range(n): #곡 수만큼
    for j in range(m+1): #볼륨
        if dp[i][j]==1: #이전 볼륨 가능 
            if j+v[i]<=m: #최대 볼륨보다 작거나 같으면
                dp[i+1][j+v[i]]=1 #1로 변경
            if j-v[i]>=0: #최소 볼륨보다 크거나 같으면
                dp[i+1][j-v[i]]=1 #1로 변경
                
for i in range(m,-1,-1): #최대 볼륨 찾기
    if dp[n][i]==1:
        max_vol=i
        break
        
print(max_vol)
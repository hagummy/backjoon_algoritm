import sys
input=sys.stdin.readline
n=int(input())
stairs=[0]
for _ in range(n):
    stairs.append(int(input()))
dp=[0]*(n+1)
if n<=2:
    print(sum(stairs))
else:
    dp[1]=stairs[1]
    dp[2]=stairs[1]+stairs[2]
    for i in range(3,n+1):
        dp[i]=max(dp[i-2]+stairs[i],dp[i-3]+stairs[i-1]+stairs[i])
    print(dp[n])
    
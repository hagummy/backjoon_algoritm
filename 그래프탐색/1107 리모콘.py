n=int(input())
m=int(input())
broken=list(map(int,input().split()))
min_cnt=abs(100-n)
for num in range(1000001):
    num=str(num)
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
        elif j==len(num)-1:
            min_cnt=min(min_cnt,abs(n-int(num))+len(str(num)))
print(min_cnt)

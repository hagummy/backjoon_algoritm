import sys
input = sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
sum_num=[0]*n
sum_num[0]=num[0]
for i in range(1,n):
    sum_num[i]=sum_num[i-1]+num[i]
print(sum_num)
case=int(input()) #범위
for i in range(case):
    st,fi=map(int,input().split())
    if st==1:
        print(sum_num[fi-1])
    else:
        print(sum_num[fi-1]-sum_num[st-2])

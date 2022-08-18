import sys
input = sys.stdin.readline
n,m=map(int,input().split())
num_to_name={}
name_to_num={}
for i in range(n):
    name=input().rstrip()
    num_to_name[i+1]=name
    name_to_num[name]=i+1

for i in range(m):
    temp=input().rstrip()
    if temp.isdigit():
        print(num_to_name[int(temp)])
    else:
        print(name_to_num[temp])
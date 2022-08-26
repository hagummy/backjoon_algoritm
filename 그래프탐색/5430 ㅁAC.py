from collections import deque
import sys
input=sys.stdin.readline
tc=int(input())
for _ in range(tc):
    order=input().rstrip()
    n=int(input())
    num=deque(input().rstrip()[1:-1].split(','))
    rev,front,back=0,0,n-1   
    flag=0
    if n==0:
        num=deque()
        front,back=0,0
    
    for i in order:
        if i=='R':
            rev+=1
        elif i=='D':
            if len(num)<1:
                flag=1
                print('error')
            else:
                if rev%2==0:
                    num.popleft()
                else:
                    num.pop()
    if flag==0:
        if rev%2==0:
            print("["+",".join(num)+']')
        else:
            num.reverse()
            print('['+','.join(num)+']')
        
                
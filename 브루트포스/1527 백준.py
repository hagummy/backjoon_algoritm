from collections import deque
a,b=map(int,input().split())
answer=0 #금민수인 것의 개수
q=deque()
q.append(4)
q.append(7)
while q:
    num=q.pop() #왼쪽의 수를 뽑아서
    if num<=b:
        if a<=num:
            answer+=1
        q.append(num*10+4)
        q.append(num*10+7)
    
print(answer)
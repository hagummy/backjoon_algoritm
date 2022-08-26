n=int(input())
def multi(n):
    num=1
    for i in range(n,0,-1):
        num*=i
    return num
answer=str(multi(n))
print(answer)
cnt=0
for i in range(len(answer)-1,0,-1):
    if answer[i]!='0':
        break
    cnt+=1
print(cnt)
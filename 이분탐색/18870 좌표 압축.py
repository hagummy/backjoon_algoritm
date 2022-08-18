n=int(input())
lst=list(map(int,input().split()))
se=set(lst)
new_lst=sorted(list(se))
print(new_lst)
answer=[]
for i in lst:
    start,end=0,len(new_lst)
    while start<=end:
        mid=(start+end)//2
        if new_lst[mid]>=i:
            end=mid-1
        else:
            start=mid+1
    answer.append(end+1)

for i in answer:
    print(i,end=' ')
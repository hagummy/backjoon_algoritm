n=int(input())
time=[]
for _ in range(n):
    st,fi=map(int,input().split())
    time.append([st,fi])
time.sort(key=lambda x:(x[1],x[0]))
cnt=0
st,fi=0,0
for start,finish in time:
    if start>=fi:
        cnt+=1
        fi=finish
    
print(cnt)
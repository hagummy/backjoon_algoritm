n,r,c=map(int,input().split())
def count(r,c,cnt,n):
    if n==1:
        return cnt
    if r<n//2 and c<n//2: #1
        return count(r,c,cnt,n//2)
    elif r<n//2 and c>=n//2: #2
        return count(r,c-n//2,cnt+(n**2)//4,n//2)
    elif r>=n//2 and c<n//2: #3
        return count(r-n//2,c,cnt+(n**2)//2,n//2)
    elif r>=n//2 and c>=n//2: #4
        return count(r-n//2,c-n//2,cnt+(n**2)-(n**2)//4,n//2)
print(count(r,c,0,2**n))
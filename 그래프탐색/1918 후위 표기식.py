n=input()
q=[]
answer=''
for letter in n:
    if letter.isalpha():
        answer+=letter
    else:
        if letter=='(':
            q.append(letter)
        elif letter=='*' or letter=='/':
            while q and (q[-1]=='*' or q=='/'):
                answer+=q.pop()
            q.append(letter)
        elif letter=='+' or letter=='-':
            while q and (q[-1]!='('):
                answer+=q.pop()
            q.append(letter)
        elif letter==')':
            while q and q[-1]!='(':
                answer+=q.pop()
            q.pop()
while q:
    answer+=q.pop()
print(answer)
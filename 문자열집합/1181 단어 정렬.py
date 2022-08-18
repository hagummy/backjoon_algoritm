n=int(input())
word=[]
for _ in range(n):
    word.append(input())
words=set(word)
word=list(words)
word.sort()
word.sort(key=len)

for i in word:
    print(i)
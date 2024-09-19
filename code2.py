n=int(input())
a = list(map(int, input().split()))
q=int(input())
b=[]
b.append(0)
c=[]
s=0
for i in range(n):
    s=b[i] ^ a[i]
    b.append(s)
for j in range(q):
    l, r = map(int, input().split())
    c.append(b[l-1] ^ b[r])
print('\n'.join(map(str, c)))
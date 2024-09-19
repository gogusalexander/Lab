def f(a,s):
    l=0
    r=len(a)-1
    while r>l+1:
        m=(l+r)//2
        if a[m]<s:
            l=m
        if a[m]>=s:
            r=m
    return r
n,k=map(int,input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:k]
a.insert(-100000000000000000,0)
a.append(10000000000000000000)
for i in range(len(b)):
    s=b[i]
    print(f(a,s))
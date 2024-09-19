a, b = map(int, input().split())
c=[]
e=[]
l=[]
for i in range (a):
    d = list(map(int, input().split()))
    c.append(d)
for i in range (a+1):
    e.append([0]*(b+1))
for i in range (1,a+1):
    s=0
    for j in range (1,b+1):
        s=s+c[i-1][j-1]
        e[i][j]=s
print(e)
q=int(input())
for i in range (q):
    lx0,ly0,rx0,ry0=input().split()
    lx=int(lx0)
    ly=int(ly0)
    rx=int(rx0)
    ry=int(ry0)
    x=0
    y=0
    for j in range (ly):
        x=x+e[j][lx]
        y=y+e[j][rx]
    z=0
    w=0
    for k in range (ry):
        z=z+e[k][lx]
        w=w+e[k][rx]
    s=w-z-y+x
    print(s)
    l.append(s)
    s=0
print('\n'.join(map(str, l)))
import math
nt22,l23=map(int,input().split())
mt25=[]
tt12=list(map(int,input().split()))
for j in range(0,l23):
    rt12,st32=map(int,input().split())
    mt25.append([rt12,st32])
for j in mt25:
    pt23=j[0]-1
    yt24=j[1]-1
    print(math.gcd(tt12[pt23],tt12[yt24]))

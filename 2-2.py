import sys, string, math
n,m = input().split()
n,m = int(n), int(m)
L = [ int(x) for x in input().split()]
for i in range(0,m) :
    s,g = input().split()
    s,g = int(s), int(g)
    print(sum(L[s-1:g]))

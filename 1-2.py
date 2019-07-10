from itertools import combinations
n,m= input().split()
m=int(m)
sha=[]
hue= combinations(n,len(n)-m)
for i in hue:
  sha.append("".join(i))
  print(min(sha))

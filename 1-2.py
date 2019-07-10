from itertools import combinations
n1,n2=input().split()
n2=int(n2)
sha=[]
hue=combinations(n1,len(n1)-n2)
for n in hue:
  sha.append("".join(n))
  print(min(sha))

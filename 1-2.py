from itertools import combinations
n1,n2=input().split()
n2=int(n2)
char=[]
nan=combinations(n1,len(n1)-n2)
for n in nan:
  char.append("".join(n))
  print(min(char))

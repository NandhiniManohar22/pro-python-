  nan,l1=map(str,input().split())
n=0
if len(nan)>len(l1):
  nan,l1=l1,nan
m=0
while m<len(nan):
  n+=(s(l1[m])-s(nan[m]))
  m+=1
for m in range(m,len(l1)):
  n+=s(l1[m])-s('a')+1
print(n)
